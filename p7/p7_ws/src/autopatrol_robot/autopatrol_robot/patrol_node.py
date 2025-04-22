from geometry_msgs.msg import PoseStamped, Pose
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from tf2_ros import TransformListener, Buffer  # 坐标监听
from tf_transformations import euler_from_quaternion, quaternion_from_euler
from autopatrol_interfaces.srv import SpeechText
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


class PatrolNode(BasicNavigator):
    def __init__(self, node_name="patrol_node"):
        super().__init__(node_name)
        self.declare_parameter("initial_point", [0.0, 0.0, 0.0])
        self.declare_parameter("target_points", [0.0, 0.0, 0.0, 1.0, 1.0, 1.57])
        self.initial_point_ = self.get_parameter("initial_point").value
        self.target_points_ = self.get_parameter("target_points").value
        self.buffer_ = Buffer()
        self.listener_ = TransformListener(self.buffer_, self)
        self.speech_client_ = self.create_client(SpeechText, "speech_text")

        # 订阅与保存图像相关定义
        self.declare_parameter("image_save_path", "")
        self.image_save_path = self.get_parameter("image_save_path").value
        self.brige = CvBridge()
        self.latest_image = None
        self.img_sub_ = self.create_subscription(
            Image, "/camera_sensor/image_raw", self.image_callback, 1
        )

    def image_callback(self, msg):
        self.latest_image = msg

    def image_record(self):
        if self.latest_image is not None:
            pose = self.get_current_pose()

            cv_image = self.brige.imgmsg_to_cv2(self.latest_image)
            cv2.imwrite(
                f"{self.image_save_path}image_{pose.translation.x:3.2f}_{pose.translation.y:3.2f}.png",
                cv_image,
            )

    def get_pose_xyyaw(self, x, y, yaw):
        pose = PoseStamped()
        pose.header.frame_id = "map"
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y

        quat = quaternion_from_euler(0, 0, yaw)
        pose.pose.orientation.x = quat[0]
        pose.pose.orientation.y = quat[1]
        pose.pose.orientation.z = quat[2]
        pose.pose.orientation.w = quat[3]
        return pose

    def init_robot_pose(self):
        # 再次定义initial_point_ ：拿到最终生效的值（yaml）、同时保持初始化和运行逻辑分离
        self.initial_point_ = self.get_parameter("initial_point").value
        self.setInitialPose(
            self.get_pose_xyyaw(
                self.initial_point_[0], self.initial_point_[1], self.initial_point_[2]
            )
        )
        self.waitUntilNav2Active()

    def get_target_points(self):
        points = []
        self.target_points_ = self.get_parameter("target_points").value
        assert len(self.target_points_) % 3 == 0
        n = int(len(self.target_points_) // 3)
        for i in range(n):
            x = self.target_points_[i * 3]
            y = self.target_points_[i * 3 + 1]
            yaw = self.target_points_[i * 3 + 2]
            points.append([x, y, yaw])
            self.get_logger().info(f"获取到目标点: {i}->({x}, {y}, {yaw})")
        return points

    def nav_to_pose(self, target_pose):
        self.waitUntilNav2Active()
        result = self.goToPose(target_pose)
        while not self.isTaskComplete():
            feedback = self.getFeedback()  # 获取状态反馈
            self.get_logger().info(f"剩余距离:{feedback.distance_remaining}")
        # 最终结果判断
        result = self.getResult()  # 获取最终结果
        self.get_logger().info(f"导航结果:{result}")

    def get_current_pose(self):
        try:
            # rclpy.time.Time：监听此刻 ；rclpy.time.Duration：timeout
            result = self.buffer_.lookup_transform(
                "base_footprint",
                "map",
                rclpy.time.Time(seconds=0),
                rclpy.time.Duration(seconds=1),
            )
            transform = result.transform

            # euler_from_quaternion输入数组
            rotation_euler = euler_from_quaternion(
                [
                    transform.rotation.x,
                    transform.rotation.y,
                    transform.rotation.z,
                    transform.rotation.w,
                ]
            )
            self.get_logger().info(f"平移{transform.translation}")
            return transform
        except Exception as e:
            self.get_logger().warn(f"获取失败原因{str(e)}")

    def speak_text(self, text):
        while not self.speech_client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f"语音服务未上线")

        request = SpeechText.Request()
        request.text = text
        future = self.speech_client_.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not True:
            respose = future.result().result
            if respose:
                self.get_logger().info(f"语音合成为:{text}")
            else:
                self.get_logger().info(f"语音合成失败")
        else:
            self.get_logger().info(f"语音合成服务请求失败")


def main():
    rclpy.init()
    patrol = PatrolNode()
    patrol.speak_text(f"正在初始化位置")
    patrol.init_robot_pose()
    patrol.speak_text(f"初始化完成")

    while rclpy.ok():
        points = patrol.get_target_points()
        for point in points:
            x, y, yaw = point[0], point[1], point[2]
            target_pose = patrol.get_pose_xyyaw(x, y, yaw)
            patrol.speak_text(f"准备前往{x},{y}")
            patrol.nav_to_pose(target_pose)
            patrol.speak_text(text=f"已到达目标点 {x},{y}, 准备记录图像")
            patrol.image_record()
            patrol.speak_text(text=f"图像记录完成")
    rclpy.shutdown()
