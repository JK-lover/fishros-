import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    # 获取默认路径
    autopatrol_robot_path = get_package_share_directory("autopatrol_robot")
    patrol_config_path = autopatrol_robot_path + "/config/patrol_config.yaml"

    action_patrol_node = Node(
        package="autopatrol_robot",
        executable="patrol_node",
        parameters=[patrol_config_path],
        output="screen",
    )

    action_patrol_speaker = Node(
        package="autopatrol_robot",
        executable="speaker",
        output="screen",
    )

    return launch.LaunchDescription(
        [
            action_patrol_node,
            action_patrol_speaker,
        ]
    )
