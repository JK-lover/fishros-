import math
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster  # 坐标发布器
from geometry_msgs.msg import TransformStamped  # 消息接口
from tf_transformations import quaternion_from_euler

class DynamicTFBroadcater(Node):

    def __init__(self):
        super().__init__('dynamic_tf_broadcaster')
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.01,self.publish_tf)

    def publish_tf(self):
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = 'camera_link'
        transform.child_frame_id = 'bottle_link'
        transform.transform.translation.x = 0.2
        transform.transform.translation.y = 0.3
        transform.transform.translation.z = 0.5

        # 欧拉转四元数
        rotation_quat = quaternion_from_euler(math.radians(0),math.radians(0),math.radians(0))
        transform.transform.rotation.x = rotation_quat[0]
        transform.transform.rotation.y = rotation_quat[1]
        transform.transform.rotation.z = rotation_quat[2]
        transform.transform.rotation.w = rotation_quat[3]

        # 发布
        self.tf_broadcaster.sendTransform(transform)
        self.get_logger().info(f'发布{transform}')


def main():
    rclpy.init()
    node = DynamicTFBroadcater()
    rclpy.spin(node)
    rclpy.shutdown()

        
