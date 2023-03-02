#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import TransformStamped
from tf2_ros.transform_broadcaster import TransformBroadcaster

from asbir_navigation.classes import *

class CameraLink(Node):
    def __init__(self):
        super().__init__('cameraLink')
        self.tfBroadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)     

    def broadcast_timer_callback(self):
        frame = TransformStamped()
        frame.header.frame_id = 'T265_pose_frame'
        frame.child_frame_id = 'D435i_link'
        self.tfBroadcaster.sendTransform(frame)

def main(args=None):
    rclpy.init(args=args)
    node = CameraLink()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
   