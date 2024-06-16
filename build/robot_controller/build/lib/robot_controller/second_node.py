#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Drawcircle(Node):
    def __init__(self):
        super().__init__("second_node_hehe")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.send_msgs)
        self.get_logger().info("Draw circle node has been started")
        
    def send_msgs(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.linear.y = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Drawcircle()
    rclpy.spin(node)
    rclpy.shutdown()
