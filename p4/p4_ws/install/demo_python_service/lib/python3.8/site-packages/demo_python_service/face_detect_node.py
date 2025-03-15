import rclpy
from rclpy.node import Node
from p4_interfaces_python.srv import FaceDetector
import face_recognition 
import cv2
from ament_index_python.packages import get_package_share_directory
import os
from cv_bridge import CvBridge
import time

class FaceDetectNode(Node):
    def __init__(self):
        super().__init__('face_detect_node')
        self.service = self.create_service(FaceDetector,'face_detect',self.detect_face_calllback)
        self.bridge = CvBridge()
        self.number_of_times_to_upsample =1
        self.model='hog'
        self.default_image_path = os.path.join(get_package_share_directory('demo_python_service'),'resource/default.jpg')
        self.get_logger().info(f"人脸检测，启动！")
        
    def detect_face_calllback(self,request,response):
        #图像格式转化为openCV下的
       if request.image.data:
            cv_image = self.bridge.imgmsg_to_cv2(request.image)
       else:
            cv_image = cv2.imread(self.default_image_path)
            self.get_logger().info(f"传入为空，使用默认图像")
       
       start_time = time.time()
       self.get_logger().info(f"加载完成，开始识别")
       #人脸位置
       face_locations = face_recognition.face_locations(cv_image,self.number_of_times_to_upsample,self.model)
       response.use_time = time.time() - start_time
       response.number = len(face_locations)
       
       #绘制人脸框
       for top,right,bottom,left in face_locations:
           response.top.append(top)
           response.right.append(right)
           response.bottom.append(bottom)
           response.left.append(left)
        
       self.get_logger().info(f"识别完成，耗时{response.use_time}秒")
       return response     #必须返回回复值
        


def main():
    rclpy.init()
    node = FaceDetectNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    