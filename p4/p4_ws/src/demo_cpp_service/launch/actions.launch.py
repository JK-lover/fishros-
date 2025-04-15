import launch
import launch.launch_description_sources
import launch_ros
from ament_index_python import get_package_share_directory
from launch.conditions import IfCondition

# 这里函数的名字不可更改
def generate_launch_description():

    action_declare_topic_list = launch.actions.DeclareLaunchArgument('topic_list',default_value='False',description='是否打印话题列表')
    topic_list = launch.substitutions.LaunchConfiguration('topic_list')
    # 1.包含其他launch
    multisim_launch_path = [get_package_share_directory('turtlesim'),'/launch/','multisim.launch.py']
    action_include_launch = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            multisim_launch_path
        )
    )
    
    # 2.打印路径
    action_log_info = launch.actions.LogInfo(msg=str(multisim_launch_path))

    # 3.执行进程
    action_executeProcess = launch.actions.ExecuteProcess(
        condition = IfCondition(topic_list),
        cmd=['ros2','topic','list'],
        output = 'screen'
    )

    # 4.组织动作
    action_group = launch.actions.GroupAction(
        [
            launch.actions.TimerAction(period=1.5, actions=[action_include_launch]),
            launch.actions.TimerAction(period=3.0, actions=[action_executeProcess])
        ]
    )

    # 合成启动描述返回
    launch_description = launch.LaunchDescription([
        action_log_info,
        action_group
    ])
    return launch_description