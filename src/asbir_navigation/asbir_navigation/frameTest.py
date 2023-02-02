#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener



class FrameListener(Node):
    def __init__(self):
        super().__init__('frame_listener')
        self.tfBuffer = Buffer()
        self.tfListener = TransformListener(self.tfBuffer, self)
        
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)
        
    def broadcast_timer_callback(self):
        o=self.tfBuffer.lookup_transform('odom_frame', 'camera_pose_frame', rclpy.time.Time())
        print(o.transform)

def main(args=None):
    rclpy.init(args=args)
    node = FrameListener()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
