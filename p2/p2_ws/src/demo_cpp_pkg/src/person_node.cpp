#include "rclcpp/rclcpp.hpp"
#include <string>
using namespace std;

class person_node : public rclcpp::Node
{
private:
    std::string m_Name;
    int m_Age;

public:
    // const..&..引用传递，既作为自类构造的参数，也传给了父类Node，避免浅拷贝的问题
    // 加入const是为了变量只读，不可修改
    person_node(const std::string &node_name, const std::string name, const int &age)
        : Node(node_name)
    {
        this->m_Name = name;
        this->m_Age = age;
    };

    void eat(const std::string &food_name)
    {
        RCLCPP_INFO(this->get_logger(), "%s,%d岁,爱吃%s",
                    this->m_Name.c_str(),
                    this->m_Age,
                    food_name.c_str());
    };
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    // makeshared相当于new,创建了一个指针，所以实例化后用node->
    auto node = std::make_shared<person_node>("person_node", "Lisa", 18);
    RCLCPP_INFO(node->get_logger(), "你好C++节点");
    node->eat("滑蛋肥牛");

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}