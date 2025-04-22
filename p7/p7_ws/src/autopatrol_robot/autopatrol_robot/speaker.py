import rclpy
from rclpy.node import Node
from autopatrol_interfaces.srv import SpeechText
import espeakng  # 相比于订阅节点，导入的库多了 时间库 time 和 语音合成库 espeakng


class Speaker(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.speech_service_ = self.create_service(
            SpeechText, "speech_text", self.speak_text_callback
        )
        self.speaker = espeakng.Speaker()
        self.speaker.voice = "zh"

    def speak_text_callback(self, request, response):
        self.get_logger().info(f"朗读{request.text}")
        self.speaker.say(request.text)
        self.speaker.wait()
        response.result = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = Speaker("novel_read")
    rclpy.spin(node)
    rclpy.shutdown()
