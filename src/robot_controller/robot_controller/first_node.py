#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Mynode(Node):
    def __init__(self):
        super().__init__("first_node_hehe")
        self.count = 0
        self.create_timer(1.0, self.timer_callback)
    def timer_callback(self):
        self.get_logger().info("Sup BOT" + str(self.count))
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = Mynode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
