import rclpy
from status_interfaces.msg import SystemStatus
from rclpy.node import Node
import psutil
import platform 

class SysStatusPub(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info("!!! 节点初始化成功 !!!")  # 关键日志
        self.status_publisher = self.create_publisher(SystemStatus,'sys_status',10)
        self.timer =  self.create_timer(1.0,self.timer_callback)  
        
    def timer_callback(self):

        cpu_percent = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        net_io_counters = psutil.net_io_counters()
        msg = SystemStatus()        
        msg.stamp = self.get_clock().now().to_msg()        
        msg.host_name = platform.node()        
        msg.cpu_percent  = cpu_percent     
        msg.memory_percent = memory_info.percent             
        msg.memory_total = memory_info.total /1024/1024             
        msg.memory_available  = memory_info.available /1024/1024     
        msg.net_sent = net_io_counters.bytes_sent /1024/1024  #换算成MB                
        msg.net_recv = net_io_counters.bytes_recv /1024/1024                       
        self.get_logger().info(f'发布：{str(msg)}')   
        self.status_publisher.publish(msg)   
        

def main(): 
    rclpy.init()
    node = SysStatusPub('System_status_pub')
    node.get_logger().info("!!! 节点已启动，进入spin循环 !!!")  # 关键日志
    try:
        rclpy.spin(node)
    except Exception as e:
        node.get_logger().error(f"Spin崩溃: {str(e)}")
    finally:
        node.destroy_node()
        rclpy.shutdown()