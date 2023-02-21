#!/usr/bin/env python3

import numpy as np
from stl import mesh

import numpy as np
import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import PointStamped
from std_msgs.msg import String
from rclpy.duration import Duration

import tf2_geometry_msgs.tf2_geometry_msgs
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_ros.transform_broadcaster import TransformBroadcaster

from asbir_navigation.classes import *

class AnalyzeObject(Node):
    def __init__(self):
            super().__init__('Graph')
            self.markerPub = self.create_publisher(MarkerArray, "visualization_marker", 10)
            self.analyzeObject()

    def analyzeObjcet(self):
        your_mesh = mesh.Mesh.from_file('top_frame2.0.STL')

        mArray = MarkerArray()
        for vector in your_mesh.data['vectors']:
            print(vector)
            # vertice = Marker()
            # vertice.header.frame_id = p.pos.header.frame_id
            # vertice.header.stamp = rclpy.time.Time().to_msg()
            # vertice.type = vertice.SPHERE
            # vertice.action = vertice.ADD
            # vertice.id = self.id
            # self.id += 1
            # vertice.scale.x = 0.01
            # vertice.scale.y = 0.01
            # vertice.scale.z = 0.01
            # vertice.pose.position.x = p.pos.point.x
            # vertice.pose.position.y = p.pos.point.y
            # vertice.pose.position.z = p.pos.point.z
            # vertice.pose.orientation.x = 0.0
            # vertice.pose.orientation.y = 0.0
            # vertice.pose.orientation.z = 0.0
            # vertice.pose.orientation.w = 1.0
            # vertice.color.r = 0.0
            # vertice.color.g = 0.0
            # vertice.color.b = 0.0
            # vertice.color.a = 1.0
        
            # mArray.markers.append(vertice)

def main(args=None):
    rclpy.init(args=args)
    graphTest = AnalyzeObject()
    rclpy.spin(graphTest)

    graphTest.destroy_node()
    rclpy.shutdown()
		
if __name__ == '__main__':
    main()
