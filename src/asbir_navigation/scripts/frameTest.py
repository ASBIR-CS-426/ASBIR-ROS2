#!/usr/bin/env python3
from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.node import Node

from tf2_ros import TransformBroadcaster
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener



class FixedFrameBroadcaster(Node):
    def __init__(self):
        super().__init__('fixed_frame_tf2_broadcaster')
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(1, self.broadcast_timer_callback)
        self.tfBuffer = Buffer()
        self.tfListener = TransformListener(self.tfBuffer, self)

    def broadcast_timer_callback(self):
        o=self.tfBuffer.lookup_transform('odom_frame', 'camera_pose_frame', rclpy.time.Time())
        print(o.transform)

def main():
    rclpy.init()
    node = FixedFrameBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
