#!/usr/bin/env python3
import os
import sys
import rclpy
from rclpy.node import Node
from asbir_navigation.classes import *
from geometry_msgs.msg import Point, PointStamped
from std_msgs.msg import Header
from builtin_interfaces.msg import Time
from rclpy.duration import Duration
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge.core import CvBridge


class ImageCompression(Node):
    def __init__(self):
            super().__init__('ImageCompression')
            self.sub = self.create_subscription(Image, '/D435i/color/image_raw', self.compressMe, 10)
            self.pub = self.create_publisher(CompressedImage, '/CompressedImage', 10)
            self.compressed = None
            self.cvBridge = CvBridge()

            self.timer = self.create_timer(1, self.broadcast_timer_callback)   


    def compressMe(self,msg):
        cv2=self.cvBridge.imgmsg_to_cv2(msg)
        self.compressed = self.cvBridge.cv2_to_compressed_imgmsg(cv2)

    def broadcast_timer_callback(self):
        if not self.compressed == None:
            print("publish")
            self.pub.publish(self.compressed)



def main(args=None):
    rclpy.init(args=args)
    node = ImageCompression()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()