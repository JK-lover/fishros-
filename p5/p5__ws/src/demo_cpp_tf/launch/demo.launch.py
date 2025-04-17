import launch
import launch_ros

# 这里函数的名字不可更改
def generate_launch_description():
   
    action_node_static_tf = launch_ros.actions.Node(
        package = 'demo_cpp_tf',
        executable = 'static_tf_broadcaster',
        output = 'log',
    )
    action_node_dynamic_tf = launch_ros.actions.Node(
        package = 'demo_cpp_tf',
        executable = 'dynamic_tf_broadcaster',
        output = 'log',
    )

    # 合成启动描述返回
    launch_description = launch.LaunchDescription([
        action_node_static_tf,
        action_node_dynamic_tf,
    ])
    return launch_description