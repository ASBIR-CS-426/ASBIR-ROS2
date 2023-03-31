#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2


class PointCloudRepublisher(Node):
    def __init__(self):
            super().__init__('ImageCompression')
            self.sub = self.create_subscription(PointCloud2, '/D435i/depth/color/points', self.subCallBack, 1)
            self.pub = self.create_publisher(PointCloud2, '/PointCloud', 1)

    def subCallBack(self,msg):
        print(msg.header.frame_id)
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PointCloudRepublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()