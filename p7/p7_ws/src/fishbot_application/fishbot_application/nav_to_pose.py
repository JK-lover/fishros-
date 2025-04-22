from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy
from rclpy.duration import Duration

def main():
    rclpy.init()
    navi = BasicNavigator()
    navi.waitUntilNav2Active()

    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navi.get_clock().now().to_msg()
    goal_pose.pose.position.x = 2.0
    goal_pose.pose.position.y = 4.0
    goal_pose.pose.orientation.w = 1.0
    
    navi.goToPose(goal_pose)
    while not navi.isTaskComplete():
        feedback = navi.getFeedback() # 获取状态反馈
        navi.get_logger().info(
            f'剩余距离:{feedback.distance_remaining}'
        )
        if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
            navi.cancelTask() # 中途取消

    # 最终结果判断
    result = navi.getResult() # 获取最终结果
    navi.get_logger().info(f'导航结果:{result}')

    # rclpy.spin(navi)
    # rclpy.shutdown()