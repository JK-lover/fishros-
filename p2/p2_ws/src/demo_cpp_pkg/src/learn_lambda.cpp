#include <iostream>
#include <algorithm>

int main()
{
    auto add = [](int a, int b) -> int
    { return a + b; };
    int sum = add(10, 20);

    // [&]表示捕获上文所有参数
    auto print_sum = [sum]() -> void
    {
        std::cout << sum << std::endl;
    };

    print_sum();
    return 0;
}