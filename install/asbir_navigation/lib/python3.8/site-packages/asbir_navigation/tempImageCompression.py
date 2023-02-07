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
import cv_bridge.core as cv


class ImageCompression(Node):
    def __init__(self):
            super().__init__('PointPub')
            self.sub = self.create_subscription(Image, '/D435i/color/image_raw', self.compressMe)
            self.pub = self.create_publisher(CompressedImage, '/CompressedImage', 10)

    def compressMe(self,msg):
        cv2=cv.imgmsg_to_cv2(msg)
        compressed = cv.cv2_to_compressed_imgmsg(cv2)

        self.pub.publish(compressed)



def main(args=None):
    rclpy.init(args=args)
    node = ImageCompression()
    rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()