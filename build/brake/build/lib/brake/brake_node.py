#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class BrakeNode(Node):
    def __init__(self):
        super().__init__('brake_node')
        self.subscriber = self.create_subscription(String, 'salut_fm', self.accept_message, 10)

    def accept_message(self, msg):
        self.get_logger().info(f"Получил сообщение {msg.data}")
        
def main():
    rclpy.init()
    node = BrakeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Нода с тормозом выключена')
    finally:
        node.destroy_node()