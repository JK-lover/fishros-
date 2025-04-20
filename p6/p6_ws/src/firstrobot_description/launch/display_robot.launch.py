import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
import launch_ros.parameter_descriptions
from launch.substitutions import Command, LaunchConfiguration
import os

# 这里函数的名字不可更改
def generate_launch_description():
    # 获取默认路径
    urdf_path = get_package_share_directory('firstrobot_description')
    default_model_path = os.path.join(urdf_path, 'urdf', 'first_robot.urdf')
    default_rviz_confi_path = os.path.join(urdf_path, 'config', 'display_model.rviz')

    # 这时的路径就成为了model对象的一个参数
    action_declare_arg_model_path = launch.actions.DeclareLaunchArgument(
        name='model',
        default_value=str(default_model_path),description='URDF的绝对路径'
    )
    
    # launch_ros.parameter_descriptions.ParameterValue：转换成参数值对象传入robot_state_publisher_node
    robot_description = launch_ros.parameter_descriptions.ParameterValue(
        # launch.substitutions.Command：功能类似于命令行
        Command(
            #  LaunchConfiguration：将路径从model中提取出来
            ['xacro ', LaunchConfiguration('model')]),
            value_type=str)
    
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable = 'robot_state_publisher',
        parameters=[{'robot_description':robot_description}]
    )

    joint_state_publisher_node  = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable = 'joint_state_publisher',
    )

    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable = 'rviz2',
        arguments = ['-d',default_rviz_confi_path]
    )

    # 合成启动描述返回
    launch_description = launch.LaunchDescription([
        action_declare_arg_model_path,
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz_node
    ])
    return launch_description