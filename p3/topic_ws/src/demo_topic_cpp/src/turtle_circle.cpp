#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <chrono>

// 进行这个声明之后可以用ms,s表示period
using namespace std::chrono_literals;

class turtle_circle_node : public rclcpp::Node
{
private:
    // 定时器
    rclcpp::TimerBase::SharedPtr timer_;
    // 创建了发布者的智能指针
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;

public:
    /// @brief 构造函数
    /// @param node_name
    turtle_circle_node(const std::string &node_name) : Node(node_name)
    {
        RCLCPP_INFO(this->get_logger(), "节点初始化完成，名称: %s", this->get_name());
        // 从rclcpp继承的create_publisher,类模板要做类型声明
        // 第一个参数：tpoic; 第二个：Qos
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);

        // 第一个参数：period; 第二个：callback
        timer_ = this->create_wall_timer(1s, std::bind(&turtle_circle_node::timer_callback, this));
    }

    // 成员函数作回调,作为信息发布
    void timer_callback()
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = 1;
        msg.linear.y = 1;
        msg.angular.z = 1;
        publisher_->publish(msg);
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<turtle_circle_node>("turtle_circle");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
