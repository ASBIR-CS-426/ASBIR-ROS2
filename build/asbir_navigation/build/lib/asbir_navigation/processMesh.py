#!/usr/bin/env python3
from stl import mesh
import numpy as np
import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
import pymesh


class ProcessMesh(Node):
    def __init__(self):
            super().__init__('ProcessMesh')
            self.markerAPub = self.create_publisher(MarkerArray, "visualization_marker_array", 10)
            self.markerPub=self.create_publisher(Marker, 'visualization_marker', 10)
            self.id=0
            self.faceArray = MarkerArray()
            self.Object = Marker()
            self.processMesh()
        

    def processMesh(self):
        # mesh = pymesh.load_mesh('/home/aralab/ASBIR-ROS2/src/objects/Cabinet.STL')
        # mesh = pymesh.load_mesh('/home/aralab/ASBIR-ROS2/src/objects/top_frame2.0.STL')
        mesh = pymesh.load_mesh('/home/aralab/ASBIR-ROS2/src/objects/bridge-final.stl')
        # meshPartition, meshCells = pymesh.partition_into_cells(mesh)

        
        for p in mesh.faces:
            face = Marker()
            face.header.frame_id = 'odom_frame'
            face.header.stamp = rclpy.time.Time().to_msg()
            face.type = face.LINE_LIST
            face.action = face.ADD
            face.id = self.id
            self.id += 1
            face.scale.x = 0.01
            face.scale.y = 0.01
            face.scale.z = 0.01
            face.pose.orientation.x = 0.0
            face.pose.orientation.y = 0.0
            face.pose.orientation.z = 0.0
            face.pose.orientation.w = 1.0
            face.color.r = 0.0
            face.color.g = 0.0
            face.color.b = 0.0
            face.color.a = 1.0
            for point in p:
                face.points.append(Point(x=mesh.vertices[point][0],y=mesh.vertices[point][1],z=mesh.vertices[point][2]))
            face.points.append(Point(x=mesh.vertices[p[0]][0],y=mesh.vertices[p[0]][1],z=mesh.vertices[p[0]][2]))

            self.faceArray.markers.append(face)

            self.Object.header.frame_id = 'odom_frame'
            self.Object.header.stamp = rclpy.time.Time().to_msg()
            self.Object.type = self.Object.MESH_RESOURCE
            self.Object.mesh_resource='file:///home/aralab/ASBIR-ROS2/src/objects/bridge-final.stl'
            self.Object.action = self.Object.ADD
            self.Object.id = self.id
            self.id += 1
            self.Object.scale.x = 1.0
            self.Object.scale.y = 1.0
            self.Object.scale.z = 1.0
            self.Object.pose.orientation.x = 0.0
            self.Object.pose.orientation.y = 0.0
            self.Object.pose.orientation.z = 0.0
            self.Object.pose.orientation.w = 1.0
            self.Object.color.r = 1.0
            self.Object.color.g = 1.0
            self.Object.color.b = 1.0
            self.Object.color.a = 1.0

            nodex =  (mesh.vertices[p[0]][0] + mesh.vertices[p[1]][0] + mesh.vertices[p[2]][0])/3
            nodey =  (mesh.vertices[p[0]][1] + mesh.vertices[p[1]][1] + mesh.vertices[p[2]][1])/3
            nodez =  (mesh.vertices[p[0]][2] + mesh.vertices[p[1]][2] + mesh.vertices[p[2]][2])/3

            
            node = Marker()
            node.header.frame_id = 'odom_frame'
            node.header.stamp = rclpy.time.Time().to_msg()
            node.type = node.SPHERE
            node.action = node.ADD
            node.id = self.id
            self.id += 1
            node.scale.x = 0.1
            node.scale.y = 0.1
            node.scale.z = 0.1
            node.pose.orientation.x = 0.0
            node.pose.orientation.y = 0.0
            node.pose.orientation.z = 0.0
            node.pose.orientation.w = 1.0
            node.pose.position.x=nodex
            node.pose.position.y=nodey
            node.pose.position.z=nodez
            node.color.r = 1.0
            node.color.g = 0.0
            node.color.b = 0.0
            node.color.a = 1.0

            self.faceArray.markers.append(node)

        self.markerAPub.publish(self.faceArray)
        self.markerPub.publish(self.Object)

            

def main(args=None):
    rclpy.init(args=args)
    processMesh = ProcessMesh()
    rclpy.spin_once(processMesh)

    processMesh.destroy_node()
    rclpy.shutdown()
		
if __name__ == '__main__':
    main()
