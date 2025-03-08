#include <iostream>
#include <functional>
#include <string>

void save_with_free_fun(const std::string &file_name)
{
    std::cout << "自由函数" << file_name << std::endl;
}

class filsave
{
public:
    void save_with_member_fun(const std::string &file_name)
    {
        std::cout << "成员函数" << file_name << std::endl;
    }
};

int main()
{
    filsave f1;

    auto save_with_lambda_fun = [](const std::string &file_name) -> void
    {
        std::cout << "lambda函数" << file_name << std::endl;
    };

    // save_with_free_fun("file.txt");
    // f1.save_with_member_fun("file.txt");
    // save_with_lambda_fun("file.txt");

    // 函数包装,实现调用方法统一
    std::function<void(const std::string &)> save1 = save_with_free_fun;
    std::function<void(const std::string &)> save2 = save_with_lambda_fun;

    // 成员函数，需要绑定,分别传入类名，成员函数，函数的占位数,将成员函数包装，防止误操作
    std::function<void(const std::string &)> save3 = std::bind(&filsave::save_with_member_fun, &f1, std::placeholders::_1);

    save1("file.txt");
    save2("file.txt");
    save3("file.txt");
    return 0;
}