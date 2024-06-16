#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Pos(Node):
    def __init__(self):
        super().__init__("pos_sub_hehe")
        self.pos_sub = self.create_subscription(Pose, "/turtle1/pose", self.pos_recv, 10)
        
    def pos_recv(self, msg: Pose):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node = Pos()
    rclpy.spin(node)
    rclpy.shutdown()
