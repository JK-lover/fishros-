import rclpy
from rclpy.node import Node
from p4_interfaces_python.srv import FaceDetector
import face_recognition 
import cv2
from ament_index_python.packages import get_package_share_directory
import os
from cv_bridge import CvBridge
import time

class FaceDetectClientNode(Node):
    def __init__(self):
        super().__init__('face_detect_client_node')
        self.bridge = CvBridge()
        self.default_image_path = os.path.join(get_package_share_directory('demo_python_service'),'resource/bus.jpg')
        self.get_logger().info(f"人脸检测的客户端启动！")
        self.client = self.create_client(FaceDetector,'face_detect')
        self.image = cv2.imread(self.default_image_path)
        
    def send_request(self):
        while self.client.wait_for_service(timeout_sec=1.0) is False:
            self.get_logger().info(f"等待客户端上线！")
            
        #构造Request
        request = FaceDetector.Request()
        request.image = self.bridge.cv2_to_imgmsg(self.image)
    
        #发送请求并等待处理完成,这里的future需等待服务端处理后赋予响应结果
        future = self.client.call_async(request)
        
        # while not future.done():
        #     time.sleep(1.0) #休眠等待服务处理,休眠线程，有可能造成死循环
        
        #rclpy.spin_until_future_complete(self,future)  
        def result_callback(result_future): 
            response = result_future.result()
            self.get_logger().info(f"接受响应，共有{response.number}张人脸，耗时{response.use_time}秒")
            self.show_response(response)
            
        future.add_done_callback(result_callback)     
        
        
    def show_response(self,response):
        for i in range(response.number):
            top = response.top[i]
            right = response.right[i]
            bottom = response.bottom [i]            
            left = response.left[i]
            cv2.rectangle(self.image,(left,top),(right,bottom),(0,0,255),5)
        #结果显示
        cv2.imshow('RESULT',self.image)
        cv2.waitKey(0)  #这里也会堵塞进程
    
        
def main():
    rclpy.init()
    node = FaceDetectClientNode()
    node.send_request()
    rclpy.spin(node)
    rclpy.shutdown()
    