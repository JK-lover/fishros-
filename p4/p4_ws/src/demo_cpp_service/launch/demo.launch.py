import launch
import launch_ros

# 这里函数的名字不可更改
def generate_launch_description():
    # 参数的声明
    action_declare_arg_background_g = launch.actions.DeclareLaunchArgument('arg_background_g',default_value="150")
    action_declare_arg_max_speed = launch.actions.DeclareLaunchArgument('arg_max_speed',default_value='2.0')

    action_node_turtle_control = launch_ros.actions.Node(
        package = 'demo_cpp_service',
        executable = 'turtle_control',
        parameters = [{'max_speed':launch.substitutions.LaunchConfiguration
                       ('arg_max_speed', default = '2.0')}],
        output = 'both',
    )
    action_node_patrol_client = launch_ros.actions.Node(
        package = 'demo_cpp_service',
        executable = 'patrol_client',
        output = 'log',
    )

    # 参数手动传给节点
    action_node_turtlesim_node = launch_ros.actions.Node(
        package = 'turtlesim',
        executable = 'turtlesim_node',
        parameters = [{'background_g':launch.substitutions.LaunchConfiguration
                       ('arg_background_g', default = "150")}],
        output = 'screen',
    )

    # 合成启动描述返回
    launch_description = launch.LaunchDescription([
        action_declare_arg_background_g,
        action_declare_arg_max_speed,
        action_node_patrol_client,
        action_node_turtle_control,
        action_node_turtlesim_node
    ])
    return launch_description