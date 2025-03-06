// #include <iostream>
// using namespace std;

// int main(int argc,char** argv)
// {
//     std::cout << "参数" << argc<< std::endl;
//     std::cout << "程序名字" << argv[0] << std::endl;

//     return 0;
// }

#include "rclcpp/rclcpp.hpp"

int main(int argc,char** argv)
{
    rclcpp::init(argc,argv);     //初始化节点

    //创建节点
    auto node = std::make_shared<rclcpp::Node>("cpp_node");
    //打印log
    RCLCPP_INFO(node->get_logger(),"你好节点");
    //循环检测
    rclcpp::spin(node);
    rclcpp::shutdown();    
    return 0;

}