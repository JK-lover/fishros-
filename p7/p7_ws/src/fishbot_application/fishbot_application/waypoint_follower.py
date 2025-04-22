from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy
from rclpy.duration import Duration

def main():
    rclpy.init()
    navi = BasicNavigator()
    navi.waitUntilNav2Active()

    goal_poses = []
    goal_pose1 = PoseStamped()
    goal_pose1.header.frame_id = 'map'
    goal_pose1.header.stamp = navi.get_clock().now().to_msg()
    goal_pose1.pose.position.x = 2.0
    goal_pose1.pose.position.y = 0.0
    goal_pose1.pose.orientation.w = 1.0
    goal_poses.append(goal_pose1)

    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id = 'map'
    goal_pose2.header.stamp = navi.get_clock().now().to_msg()
    goal_pose2.pose.position.x = 2.0
    goal_pose2.pose.position.y = 1.0
    goal_pose2.pose.orientation.w = 0.0
    goal_poses.append(goal_pose2)

    goal_pose3 = PoseStamped()
    goal_pose3.header.frame_id = 'map'
    goal_pose3.header.stamp = navi.get_clock().now().to_msg()
    goal_pose3.pose.position.x = 0.0
    goal_pose3.pose.position.y = 0.0
    goal_pose3.pose.orientation.w = 1.0
    goal_poses.append(goal_pose3)
    
    navi.followWaypoints(goal_poses)
    while not navi.isTaskComplete():
        feedback = navi.getFeedback() # 获取状态反馈
        navi.get_logger().info(
            f'编号:{feedback.current_waypoint}'
        )

    # 最终结果判断
    result = navi.getResult() # 获取最终结果
    navi.get_logger().info(f'导航结果:{result}')

    # rclpy.spin(navi)
    # rclpy.shutdown()