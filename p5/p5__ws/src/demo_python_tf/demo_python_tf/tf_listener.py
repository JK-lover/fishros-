import math
import rclpy
from rclpy.node import Node
import rclpy.time
from tf2_ros import TransformListener,Buffer  # 坐标监听
from tf_transformations import euler_from_quaternion

class TFListener(Node):

    def __init__(self):
        super().__init__('tf_listener')
        self.buffer_ = Buffer()
        self.listener_ = TransformListener(self.buffer_,self)
        self.timer_ = self.create_timer(1,self.get_transfrom)

    def get_transfrom(self):
        try:
            # rclpy.time.Time：监听此刻 ；rclpy.time.Duration：timeout
            result = self.buffer_.lookup_transform('base_link','bottle_link',rclpy.time.Time(seconds=0),rclpy.time.Duration(seconds=1))
            transform = result.transform

            # euler_from_quaternion输入数组
            rotation_euler = euler_from_quaternion([
                transform.rotation.x,
                transform.rotation.y,
                transform.rotation.z,
                transform.rotation.w,
            ])
            self.get_logger().info(f'平移{transform.translation},四元数{transform.rotation},欧拉{rotation_euler}')
        except Exception as e:
            self.get_logger().warn(f'获取失败原因{str(e)}')


def main():
    rclpy.init()
    node = TFListener()
    rclpy.spin(node)
    rclpy.shutdown()

        
