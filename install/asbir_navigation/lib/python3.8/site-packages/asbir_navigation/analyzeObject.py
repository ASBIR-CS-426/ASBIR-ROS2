#!/usr/bin/env python3
from stl import mesh
import numpy as np
import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
import pymesh


class AnalyzeObject(Node):
    def __init__(self):
            super().__init__('Graph')
            self.markerAPub = self.create_publisher(MarkerArray, "visualization_marker_array", 10)
            self.markerPub = self.create_publisher(Marker, "visualization_marker", 10)
            self.id=0
            self.verticeArray = MarkerArray()
            # self.triangle = Marker()
            self.analyzeObject()
            
            # self.timer = self.create_timer(1, self.broadcast_timer_callback) 

    def analyzeObject(self):
        mesh = pymesh.load_mesh('/home/aralab/ASBIR-ROS2/src/objects/top_frame2.0.STL')
        print(mesh.num_voxels)
        # mesh = pymesh.load_mesh('/home/aralab/ASBIR-ROS2/src/objects/Cabinet.STL')
        V, E = pymesh.mesh_to_graph(mesh)
        print(len(V))
        # print(E)

        # for p in mesh.vertices:
        #     # print(p)
        #     vertice = Marker()
        #     vertice.header.frame_id = 'odom_frame'
        #     vertice.header.stamp = rclpy.time.Time().to_msg()
        #     vertice.type = vertice.SPHERE
        #     vertice.action = vertice.ADD
        #     vertice.id = self.id
        #     self.id += 1
        #     vertice.scale.x = 0.01
        #     vertice.scale.y = 0.01
        #     vertice.scale.z = 0.01
        #     # vertice.pose.position.x = p.pos.point.x
        #     # vertice.pose.position.y = p.pos.point.y
        #     # vertice.pose.position.z = p.pos.point.z
        #     vertice.pose.orientation.x = 0.0
        #     vertice.pose.orientation.y = 0.0
        #     vertice.pose.orientation.z = 0.0
        #     vertice.pose.orientation.w = 1.0
        #     vertice.color.r = 0.0
        #     vertice.color.g = 0.0
        #     vertice.color.b = 0.0
        #     vertice.color.a = 1.0
        #     # if p.edge:
        #     # 	vertice.color.r = 0.5
        #     # 	vertice.color.g = 0
        #     # 	vertice.color.b = 1
        #     # 	vertice.color.a = 1
        #     self.verticeArray.markers.append(vertice)

def main(args=None):
    rclpy.init(args=args)
    graphTest = AnalyzeObject()
    rclpy.spin_once(graphTest)

    graphTest.destroy_node()
    rclpy.shutdown()
		
if __name__ == '__main__':
    main()
