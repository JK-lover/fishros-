import launch
import launch.event_handlers
import launch_ros
from ament_index_python.packages import get_package_share_directory
import launch_ros.parameter_descriptions
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
import os

# 这里函数的名字不可更改
def generate_launch_description():
    # 机器人名字
    robot_name_in_model = "fishbot"
    # 获取默认路径
    urdf_path = get_package_share_directory('firstrobot_description')
    default_model_path = os.path.join(urdf_path, 'urdf', 'fishbot/fishbot.urdf.xacro')
    default_gazebo_path = os.path.join(urdf_path, 'world', 'custom_room.world')

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
    
    robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable = 'robot_state_publisher',
        parameters=[{'robot_description':robot_description}]
    )

    # 包含启动环境的launch
    launch_gazebo = launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('gazebo_ros'),'/launch','/gazebo.launch.py']),
        launch_arguments=[('world',default_gazebo_path),('verbose','true')]
    )

    # 加载机器人
    spawn_entity_node = launch_ros.actions.Node(
        package='gazebo_ros',
        executable = 'spawn_entity.py',
        arguments=['-topic','/robot_description',
                    '-entity',robot_name_in_model, ]
    )

    # 声明一个执行子进程的 Action，加载并激活 fishbot_joint_state_broadcaster 控制器
    load_joint_state_controller = launch.actions.ExecuteProcess(
        cmd='ros2 control load_controller fishbot_joint_state_broadcaster --set-state active'.split(' '),
        output='screen',
    )

    # # 加载并激活 fishbot_effort_controller 控制器
    # load_fishbot_effort_controller = launch.actions.ExecuteProcess(
    #     cmd='ros2 control load_controller fishbot_effort_controller --set-state active'.split(' '),
    #     output='screen',
    # )

    # 加载并激活 fishbot_diff_drive_controller 控制器
    load_fishbot_diff_drive_controller = launch.actions.ExecuteProcess(
        cmd='ros2 control load_controller fishbot_diff_drive_controller --set-state active'.split(' '),
        output='screen',
    )
    
    # 合成启动描述返回
    launch_description = launch.LaunchDescription([
        action_declare_arg_model_path,
        robot_state_publisher,
        launch_gazebo,
        spawn_entity_node,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=spawn_entity_node,
                on_exit=[load_joint_state_controller],
            )
        ),
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=load_joint_state_controller,
                # 防止冲突，注释掉力控制器
                # on_exit=[load_fishbot_effort_controller],
                on_exit=[load_fishbot_diff_drive_controller],
            )
        ),
    ])
    return launch_description