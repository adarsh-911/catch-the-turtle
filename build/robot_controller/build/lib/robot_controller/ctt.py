#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from functools import partial
import random

class Pos(Node):
    def __init__(self):
        super().__init__("catch_it_hehe")
        self.prev_x = 2.0
        self.prev_y = 3.0
        self.points = 0
        self.buffer = 0
        self.call_spawn_serv(2.0,3.0,0.0)
        self.pos_sub = self.create_subscription(Pose, "/turtle1/pose", self.pos_recv, 10)
        
    def pos_recv(self, pos: Pose):
        #self.get_logger().info(str(msg))
        buffer += 1
        if buffer == 50:
            if abs(pos.x - prev_x) <= 0.5 or abs(pos.y - prev_y) <= 0.5:
            prev_x = random.uniform(1,11)
            prev_y = random.uniform(1,11)
            self.call_spawn_serv(prev_x,prev_y,0.0)
            points += 1
            self.get_logger().info(points)
        buffer = 0

    def call_spawn_serv(self,x,y,theta):
        client = self.create_client(Spawn, "/spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service...")

        req = Spawn.Request()
        req.x = x
        req.y = y
        req.theta = theta
        #req.name = name

        future = client.call_async(request)
        future.add_done_callback(partial(self.call_spawn))

    def call_spawn(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed : %r"% (e,))

def main(args=None):
    rclpy.init(args=args)
    node = Pos()
    rclpy.spin(node)
    rclpy.shutdown()
