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
        self.default_image_path = os.path.join(get_package_share_directory('demo_python_service'),'resource/default.jpg')
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

"""改进版本，实现对文件夹下的指定文件进行检测"""    
# import rclpy
# from rclpy.node import Node
# from p4_interfaces_python.srv import FaceDetector
# import cv2
# from ament_index_python.packages import get_package_share_directory
# import os
# from cv_bridge import CvBridge
# import time

# class FaceDetectClientNode(Node):
#     def __init__(self):
#         super().__init__('face_detect_client_node')
#         self.bridge = CvBridge()
#         # 获取资源目录路径
#         self.resource_dir = os.path.join(
#             get_package_share_directory('demo_python_service'),
#             'resource'
#         )
#         self.default_image_path = os.path.join(self.resource_dir, 'default.jpg')
#         self.get_logger().info(f"人脸检测的客户端启动！")
#         self.client = self.create_client(FaceDetector, 'face_detect')
#         self.image = None  # 初始化时先不加载图片
#         # 添加定时器处理OpenCV窗口事件
#         self.timer = self.create_timer(0.1, self.handle_opencv_events)

#     def handle_opencv_events(self):
#         """定时处理OpenCV窗口事件"""
#         cv2.waitKey(1)

#     def send_request(self, image_path):
#         """ 发送请求的改进版本 """
#         # 加载图片
#         if not os.path.exists(image_path):
#             self.get_logger().error(f"文件 {image_path} 不存在，使用默认图片")
#             image_path = self.default_image_path
            
#         self.image = cv2.imread(image_path)
#         if self.image is None:
#             self.get_logger().error("图片加载失败，使用默认图片")
#             self.image = cv2.imread(self.default_image_path)

#         # 等待服务可用
#         while not self.client.wait_for_service(timeout_sec=1.0):
#             self.get_logger().info("等待服务端上线...")

#         # 构造请求
#         request = FaceDetector.Request()
#         request.image = self.bridge.cv2_to_imgmsg(self.image)
        
#         # 异步调用
#         future = self.client.call_async(request)
#         future.add_done_callback(self.result_callback)

#     def result_callback(self, future): 
#         try:
#             response = future.result()
#             self.get_logger().info(
#                 f"检测到 {response.number} 张人脸，耗时 {response.use_time:.2f} 秒"
#             )
#             self.show_response(response)
#         except Exception as e:
#             self.get_logger().error(f"服务调用失败: {e}")

#     def show_response(self, response):
#         # 绘制所有人脸框
#         for i in range(response.number):
#             top = response.top[i]
#             right = response.right[i]
#             bottom = response.bottom[i]
#             left = response.left[i]
#             cv2.rectangle(
#                 self.image,
#                 (left, top), 
#                 (right, bottom),
#                 (0, 0, 255), 
#                 5
#             )
        
#         # 显示结果窗口
#         cv2.imshow('RESULT', self.image)
#         # 确保窗口创建后立即显示
#         cv2.waitKey(1)

# def main():
#     rclpy.init()
#     node = FaceDetectClientNode()
    
#     try:
#         # 获取用户输入
#         filename = input("请输入resource目录下的图片文件名（例如 test.jpg）：").strip()
#         resource_dir = node.resource_dir  # 复用节点中的资源目录路径
#         selected_image_path = os.path.join(resource_dir, filename)
        
#         # 发送请求
#         node.send_request(selected_image_path)
        
#         # 保持节点运行
#         rclpy.spin(node)
        
#     finally:
#         # 清理资源
#         cv2.destroyAllWindows()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()    