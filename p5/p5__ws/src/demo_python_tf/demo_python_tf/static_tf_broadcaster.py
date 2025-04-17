import math
import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster  # 静态坐标发布器
from geometry_msgs.msg import TransformStamped  # 消息接口
from tf_transformations import quaternion_from_euler

class StaticTFBroadcater(Node):

    def __init__(self):
        super().__init__('static_tf_broadcaster')
        self.static_broadcaster = StaticTransformBroadcaster(self)
        self.publish_static_tf()

    def publish_static_tf(self):
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = 'base_link'
        transform.child_frame_id = 'camera_link'
        transform.transform.translation.x = 0.5
        transform.transform.translation.y = 0.3
        transform.transform.translation.z = 0.6

        # 欧拉转四元数
        rotation_quat = quaternion_from_euler(math.radians(180),math.radians(0),math.radians(0))
        transform.transform.rotation.x = rotation_quat[0]
        transform.transform.rotation.y = rotation_quat[1]
        transform.transform.rotation.z = rotation_quat[2]
        transform.transform.rotation.w = rotation_quat[3]

        # 发布
        self.static_broadcaster.sendTransform(transform)
        self.get_logger().info(f'发布{transform}')


def main():
    rclpy.init()
    node = StaticTFBroadcater()
    rclpy.spin(node)
    rclpy.shutdown()

        
