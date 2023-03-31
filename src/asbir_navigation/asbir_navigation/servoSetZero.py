#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from asbir_navigation.classes import *
from geometry_msgs.msg import Point, PointStamped
from std_msgs.msg import Header, Float32MultiArray
from builtin_interfaces.msg import Time
from rclpy.duration import Duration


class SetZero(Node):
    def __init__(self):
            super().__init__('setZero')
            self.ctrlPub = self.create_publisher(PointStamped, 'servoControl', 1)
            self.timer = self.create_timer(1, self.broadcast_timer_callback)     

    def broadcast_timer_callback(self):
        ctrlarr = Float32MultiArray(data=[90,90,0,0])
        self.ctrlPub.publish(ctrlarr)



def main(args=None):
    rclpy.init(args=args)
    node = SetZero()
    rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()