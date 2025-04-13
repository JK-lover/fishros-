#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <chrono>
#include "turtlesim/msg/pose.hpp"
#include "p4_interfaces_python/srv/patrol.hpp"
#include "rcl_interfaces/msg/set_parameters_result.hpp"

using SetParametersResult = rcl_interfaces::msg::SetParametersResult;
using Patrol = p4_interfaces_python::srv::Patrol;

// 进行这个声明之后可以用ms,s表示period
using namespace std::chrono_literals;

class turtle_control_node : public rclcpp::Node
{
private:
    //  声明参数回调的智能指针
    OnSetParametersCallbackHandle::SharedPtr parameters_callback_handle;
    // 创建服务端智能指针
    rclcpp::Service<Patrol>::SharedPtr patrol_service_;
    // 创建了发布者的智能指针
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    // 创建订阅者指针
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscribor_;

    double target_x{3.0};
    double target_y{2.0};

    // PID参数
    double kp{1.0}; // 原比例系数k改名为kp
    double ki{0.0}; // 新增积分系数
    double kd{0.5}; // 新增微分系数

    // PID状态变量
    double integral{0.0};   // 积分累积值
    double prev_error{0.0}; // 上一次的误差
    rclcpp::Time prev_time; // 上一次的时间戳

    double max_speed{3.0};

public:
    /// @brief 构造函数
    /// @param node_name
    turtle_control_node(const std::string &node_name) : Node(node_name),
                                                        prev_time(this->get_clock()->now()) // 初始化时间戳
    {
        this->declare_parameter("kp", 1.0);
        this->declare_parameter("ki", 0.0);
        this->declare_parameter("kd", 0.5);
        this->declare_parameter("max_speed", 3.0);

        this->get_parameter("kp", kp);
        this->get_parameter("ki", ki);
        this->get_parameter("kd", kd);
        this->get_parameter("max_speed", max_speed);

        // this->set_parameter
        parameters_callback_handle = this->add_on_set_parameters_callback([&](const std::vector<rclcpp::Parameter> &params) -> SetParametersResult
                                                                          {
                                                                            for (const auto & param : params) {
                                                                                RCLCPP_INFO(this->get_logger(),"更新参数 %s为 %f",param.get_name().c_str(),param.as_double());
                                                                                if(param.get_name() == "kp"){
                                                                                    kp = param.as_double();
                                                                                }else if(param.get_name() == "ki"){
                                                                                    ki = param.as_double();
                                                                                }else if(param.get_name() == "kd"){
                                                                                    kd = param.as_double();
                                                                                }else if(param.get_name() == "max_speed"){
                                                                                    max_speed = param.as_double();
                                                                                }
                                                                            } 
                                                                            auto result = SetParametersResult();
                                                                            result.successful = true;
                                                                            return result; });

        RCLCPP_INFO(this->get_logger(), "节点初始化完成，名称: %s", this->get_name());
        // 从rclcpp继承的create_publisher,类模板要做类型声明
        // 第一个参数：tpoic; 第二个：Qos
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);

        // 第一个参数：tpoic_name; 第二个：Qos; callback; 站位符;
        subscribor_ = this->create_subscription<turtlesim::msg::Pose>("/turtle1/pose",
                                                                      10,
                                                                      std::bind(&turtle_control_node::on_pose_received, this, std::placeholders::_1));

        patrol_service_ = this->create_service<Patrol>("patrol", [&](const Patrol::Request::SharedPtr request, Patrol::Response::SharedPtr response) -> void
                                                       {      
                                                        if(
                                                            (0<this->target_x && this->target_x<12.0f)&&
                                                            (0<this->target_y && this->target_y<12.0f)
                                                        ){
                                                            this->target_x = request->target_x;
                                                            this->target_y = request->target_y;
                                                            response->result = Patrol::Response::SUCCESS;

                                                            // 重置PID状态
                                                            integral = 0.0;
                                                            prev_error = 0.0;
                                                            prev_time = this->get_clock()->now(); 
                                                        }else{
                                                            response->result = Patrol::Response::FAIL;
                                                        } });
    }

    // 参数是收到数据的共享指针
    void on_pose_received(const turtlesim::msg::Pose::SharedPtr pose)
    {
        // 1. 计算时间间隔 dt
        auto current_time = this->get_clock()->now();
        double dt = (current_time - prev_time).seconds();
        if (dt <= 0)
            dt = 0.01; // 防止零除

        // 2.获取当前位置
        auto current_x = pose->x;
        auto current_y = pose->y;
        RCLCPP_INFO(get_logger(), "当前:x=%f,y=%f", current_x, current_y);

        // 3.计算距离差和角度差
        auto error_x = target_x - current_x;
        auto error_y = target_y - current_y;

        auto distance = std::sqrt(error_x * error_x + error_y * error_y);
        auto error = distance; // PID的误差信号为距离
        auto angle = std::atan2(error_y, error_x) - pose->theta;

        // 4. 计算PID三项
        integral += error * dt;                        // 积分项
        integral = std::clamp(integral, -1.0, 1.0);    // 积分限幅防止饱和
        double derivative = (error - prev_error) / dt; // 微分项

        // 5. 计算控制信号
        double control = kp * error + ki * integral + kd * derivative;
        control = std::clamp(control, -max_speed, max_speed); // 限速

        // 6.控制律
        auto msg = geometry_msgs::msg::Twist();
        if (distance > 0.1)
        {
            if (fabs(angle) > 0.2)
            {
                msg.angular.z = angle;
            }
            else
            {
                msg.linear.x = control;
            }
        }

        // 7.发布信息
        publisher_->publish(msg);
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<turtle_control_node>("turtle_control");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
