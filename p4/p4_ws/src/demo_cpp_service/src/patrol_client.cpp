#include "rclcpp/rclcpp.hpp"
#include "p4_interfaces_python/srv/patrol.hpp"
#include <chrono>
#include <ctime>

using Patrol = p4_interfaces_python::srv::Patrol;
// 进行这个声明之后可以用ms,s表示period
using namespace std::chrono_literals;

class PatrolClient : public rclcpp::Node
{
private:
    // 声明指针
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Client<Patrol>::SharedPtr patrol_client_;

public:
    /// @brief 构造函数
    /// @param node_name
    PatrolClient() : Node("patrol_client")
    {
        // 初始化随机种子
        srand(time(NULL));

        // 客户端名字与服务端保持一致
        patrol_client_ = this->create_client<Patrol>("patrol");

        // 定时器初始化,第一个参数：period; 第二个：callback
        timer_ = this->create_wall_timer(10s, [&]() -> void
                                         {
            //1.等待服务上线
            while (!patrol_client_->wait_for_service(1s))
            {
                //每秒检测一次服务端是否有效
                if(!rclcpp::ok()){
                    RCLCPP_ERROR(this->get_logger(),"等待服务中被打断");
                    return;
                }
                RCLCPP_INFO(this->get_logger(),"等待服务上线");
            }
            
            //2.构造请求对象
            auto request = std::make_shared<Patrol::Request>();
            request->target_x = rand() % 15;
            request->target_y = rand() % 15;
            RCLCPP_INFO(this->get_logger(),"准备好了随机点%f,%f",request->target_x,request->target_y);

            //3.发送异步请求,async_send_request返回一个类型为SharedFuture的对象，用对象的get函数获取服务端输出结果
            patrol_client_ ->async_send_request(request,[&](rclcpp::Client<Patrol>::SharedFuture result_future)->void{
                auto response = result_future.get();
                if(response->result == Patrol::Response::SUCCESS)
                {
                    RCLCPP_INFO(this->get_logger(),"目标处理成功");
                }
                else if (response->result == Patrol::Response::FAIL)
                {
                    RCLCPP_INFO(this->get_logger(),"目标处理失败");
                }
            }); });
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PatrolClient>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
