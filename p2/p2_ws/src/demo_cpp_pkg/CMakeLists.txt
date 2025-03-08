cmake_minimum_required(VERSION 3.8)
project(demo_cpp_pkg)  # 确保与 package.xml 的 <name> 一致

# 设置 C++17 标准
set(CMAKE_CXX_STANDARD 17)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(cpp_node src/cpp_node.cpp)
add_executable(person_node src/person_node.cpp)
add_executable(learn_auto src/learn_auto.cpp)
add_executable(learn_shared src/learn_shared.cpp)
add_executable(learn_lambda src/learn_lambda.cpp)
add_executable(learn_functional src/learn_functional.cpp)

ament_target_dependencies(cpp_node rclcpp)
ament_target_dependencies(person_node rclcpp)

# 修正安装路径
install(TARGETS
  cpp_node person_node learn_auto learn_shared learn_lambda learn_functional
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
