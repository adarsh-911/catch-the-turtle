#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from functools import partial
import random

class Pos(Node):
    def __init__(self):
        super().__init__("catch_it_hehe")
        self.prev_x = 2.0
        self.prev_y = 3.0
        self.points = 0
        self.buffer = 0
        self.ini = 0
        self.delay = 0
        #self.call_spawn_serv(2.0,3.0,0.0)
        self.pos_sub = self.create_subscription(Pose, "/turtle1/pose", self.pos_recv, 10)
        
    def pos_recv(self, pos: Pose):
        if self.ini == 0:
            self.call_spawn_serv(2.0,3.0,0.0,'john0')
            self.ini = 1
        self.buffer += 1
        if self.buffer == 20:
            if (((pos.x - self.prev_x)**2 + (pos.y - self.prev_y)**2) <= 0.5):
                self.prev_x = random.uniform(1,10)
                self.prev_y = random.uniform(1,10)
                self.call_kill_serv('john'+str(self.points))
                self.points += 1
                self.call_spawn_serv(self.prev_x, self.prev_y, 0.0,'john'+str(self.points))
                self.get_logger().info("Turtle hit : Points = " + str(self.points))
            self.buffer = 0

    def call_spawn_serv(self,x,y,theta,name):
        client = self.create_client(Spawn, "/spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service...")

        req = Spawn.Request()
        req.x = x
        req.y = y
        req.theta = theta
        req.name = name

        future = client.call_async(req)
        future.add_done_callback(partial(self.call_spawn))

    def call_spawn(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed : %r"% (e,))

    def call_kill_serv(self,name):
        client2 = self.create_client(Kill, "/kill")
        while not client2.wait_for_service(1.0):
           self.get_logger().warn("Waiting for service...")

        req2 = Kill.Request()
        req2.name = name
        future2 = client2.call_async(req2)
        future2.add_done_callback(partial(self.call_kill))

    def call_kill(self, future2):
        try:
            response = future2.result()
        except Exception as e:
            self.get_logger().error("Service call failed : %r"% (e,))


def main(args=None):
    rclpy.init(args=args)
    node = Pos()
    rclpy.spin(node)
    rclpy.shutdown()
