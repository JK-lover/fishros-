cmake_minimum_required(VERSION 3.8)
project(demo_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)           #查找到对应头文件和库文件
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

add_executable(p2 src/p2.cpp)
#message(STATUS ${rclcpp_INCLUDE_DIRS})  #头文件
#message(STATUS ${rclcpp_LIBRARIES})     #库文件

#target_include_directories(p2 PUBLIC ${rclcpp_INCLUDE_DIRS}) #头文件包含
#target_link_libraries(p2 ${rclcpp_LIBRARIES})                #库文件连接
ament_target_dependencies(p2 rclcpp)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
