#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <chrono>
#include "turtlesim/msg/pose.hpp"

// 进行这个声明之后可以用ms,s表示period
using namespace std::chrono_literals;

class turtle_control_node : public rclcpp::Node
{
private:
    // 创建了发布者的智能指针
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    // 创建订阅者指针
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscribor_;

    double target_x{3.0};
    double target_y{2.0};
    double k{1.0}; // 比例系数
    double max_speed{3.0};

public:
    /// @brief 构造函数
    /// @param node_name
    turtle_control_node(const std::string &node_name) : Node(node_name)
    {
        RCLCPP_INFO(this->get_logger(), "节点初始化完成，名称: %s", this->get_name());
        // 从rclcpp继承的create_publisher,类模板要做类型声明
        // 第一个参数：tpoic; 第二个：Qos
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);

        // 第一个参数：tpoic_name; 第二个：Qos; callback; 站位符;
        subscribor_ = this->create_subscription<turtlesim::msg::Pose>("/turtle1/pose",
                                                                      10,
                                                                      std::bind(&turtle_control_node::on_pose_received, this, std::placeholders::_1));
    }

    // 参数是收到数据的共享指针
    void on_pose_received(const turtlesim::msg::Pose::SharedPtr pose)
    {
        // 1.获取当前位置
        auto current_x = pose->x;
        auto current_y = pose->y;
        RCLCPP_INFO(get_logger(), "当前:x=%f,y=%f", current_x, current_y);
        // 2.计算距离差和角度差
        auto error_x = target_x - current_x;
        auto error_y = target_y - current_y;

        auto distance = std::sqrt(error_x * error_x + error_y * error_y);
        auto angle = std::atan2(error_y, error_x) - pose->theta;

        // 3.控制律
        auto msg = geometry_msgs::msg::Twist();
        if (distance > 0.1)
        {
            if (fabs(angle) > 0.2)
            {
                msg.angular.z = angle;
            }
            else
            {
                msg.linear.x = k * distance;
            }
        }

        // 4.限制速度最大值
        if (msg.linear.x > max_speed)
        {
            msg.linear.x = max_speed;
        }

        // 5.发布信息
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
