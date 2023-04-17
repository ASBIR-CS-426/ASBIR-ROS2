#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from asbir_navigation.classes import *
from geometry_msgs.msg import Point, PointStamped
from std_msgs.msg import Header
from builtin_interfaces.msg import Time
from rclpy.duration import Duration
import tf2_ros
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class PointPub(Node):
    def __init__(self):
            super().__init__('PointPub')
            self.tfBuffer = Buffer()
            self.tfListener = TransformListener(self.tfBuffer, self)
            self.timer = self.create_timer(1, self.broadcast_timer_callback)     


    def broadcast_timer_callback(self):
        try:
            transform=self.tfBuffer.lookup_transform("odom_frame", "structure", rclpy.time.Time())
            print(transform)
        except tf2_ros.LookupException:
            return



def main(args=None):
    rclpy.init(args=args)
    node = PointPub()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()