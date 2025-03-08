#include <iostream>
#include <memory>
using namespace std;
int main()
{
    // make_shared<数据类型/类>（参数）,返回值类型shared_ptr<std::string>
    auto p1 = std::make_shared<std::string>("This is str.");
    std::cout << "p1引用计数" << p1.use_count() << "，内存地址" << p1.get() << std::endl;

    auto p2 = p1;
    // 该引用计数表示指向内存地址的指针数量
    std::cout << "p1引用计数" << p1.use_count() << "，内存地址" << p1.get() << std::endl;
    std::cout << "p2引用计数" << p2.use_count() << "，内存地址" << p2.get() << std::endl;

    // 释放引用
    p1.reset();
    std::cout << "p1引用计数" << p1.use_count() << "，内存地址" << p1.get() << std::endl;
    std::cout << "p2引用计数" << p2.use_count() << "，内存地址" << p2.get() << std::endl;

    std::cout << p2->c_str() << endl;
    return 0;
}