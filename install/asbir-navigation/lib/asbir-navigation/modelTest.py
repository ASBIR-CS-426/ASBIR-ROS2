#!/usr/bin/env python3
import numpy as np
import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Quaternion, Transform, TransformStamped, Pose, Vector3, Vector3Stamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32MultiArray, Bool, String
from rclpy_message_converter import message_converter

import tf2_ros 
import tf2_geometry_msgs
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from tf2_ros.transform_broadcaster import TransformBroadcaster

from asbir-navigation.classes import *

class ModelTest(Node):
    def __init__(self):
            super().__init__('ModelGraph')
            self.rate = self.create_rate(2)
            self.graphPub = self.create_publisher(String, 'model_graph', 10)
            self.markerPub = self.create_publisher(Marker, "visualization_marker", 10)
            self.markerAPub = self.create_publisher(MarkerArray, "visualization_marker_array", 10)
            self.tfBuffer = Buffer()
            self.tfListener = TransformListener(self.tfBuffer, self)
            self.tfSurfaceStaticBroadcaster = StaticTransformBroadcaster(self)
            self.tfPointStaticBroadcaster = StaticTransformBroadcaster(self)

            self.graph = {}
            self.points = []
            self.id = 0
            
            # self.tfBuffer.registration.add(PointStamped)
            self.pathModel()

    def pathModel(self):
        
        F = FindEdge()
        S = Surfaces()
        verticeArray=MarkerArray()

        # broadcast frames of surface
        self.tfSurfaceStaticBroadcaster.sendTransform([S.surfaceA.getFrame(Quaternion(x=0.0,y=0.0,z=0.0,w=1.0)), 
                                S.surfaceB.getFrame(Quaternion(x=0.0, y=-0.707, z=0.0, w=0.707)),
                                S.surfaceC.getFrame(Quaternion(x=0.707, y=0.0, z=0.707, w=0.0)),
                                S.surfaceD.getFrame(Quaternion(x=0.5, y=-0.5, z=0.5, w=0.5))])

        #====Build Structure Model===
        # Create base surface model
        surface=Marker()
        # surface.header.frame_id = "robot_odom_frame"
        # surface.header.frame_id = "camera_odom_frame"
        surface.header.frame_id = "odom_frame"
        surface.header.stamp = rclpy.time.Time().to_msg()
        surface.ns = "Namespace"
        surface.id = self.id
        surface.type = surface.CUBE
        surface.action = surface.ADD
        surface.scale.x = S.xDim
        surface.scale.y = S.yDim
        surface.scale.z = S.zDim
        surface.pose.position.x = S.xDim/2 + S.xOffset
        surface.pose.position.y = S.yDim/2 + S.yOffset
        surface.pose.position.z = S.zDim/2 + S.zOffset
        surface.pose.orientation.x = 0.0
        surface.pose.orientation.y = 0.0
        surface.pose.orientation.z = 0.0
        surface.pose.orientation.w = 1.0
        surface.color.r = 0.5
        surface.color.g = 0.5
        surface.color.b = 0.5
        surface.color.a = 1.0
        self.id += 1
        
        #===Create Vertices===
        row,col = (2, 3)
        
        for i in range(row+1):
            for j in range(col):
                p = Vertice(TransformStamped(),S.surfaceA)
                p.frame_pos.header.frame_id = 'surfaceA'
                p.frame_pos.header.stamp = rclpy.time.Time().to_msg()
                p.id = "%s_%d_%d" %('surfaceA', i, j)
                p.frame_pos.transform.translation.x = (S.xDim/row) * (i)
                p.frame_pos.transform.translation.y = (S.yDim/col) * (j)
                p.frame_pos.transform.translation.z = 0.0
                p.frame_pos.child_frame_id = p.frame_pos.header.frame_id+str(p.frame_pos.transform.translation)
                if (p.frame_pos.transform.translation.x == S.xDim or p.frame_pos.transform.translation.x == 0) and not (p.frame_pos.transform.translation.y == S.yDim or p.frame_pos.transform.translation.y == 0):
                    p.edge = True
                elif (p.frame_pos.transform.translation.y == S.yDim or p.frame_pos.transform.translation.y == 0) and not (p.frame_pos.transform.translation.x == S.xDim or p.frame_pos.transform.translation.x == 0):
                    p.edge = True
                if not ((i == row and j == col) or (i == 0 and j == col) or (i == row and j ==0) or (i == 0 and j == 0)):
                    self.points.append(p)

        row,col = (6, 3)
        for i in range(row):
            for j in range(1,col):
                p = Vertice(TransformStamped(),S.surfaceB)
                p.frame_pos.header.frame_id = 'surfaceB'
                p.frame_pos.header.stamp = rclpy.time.Time().to_msg()
                p.id = "%s_%d_%d" %('surfaceB', i, j)
                p.frame_pos.transform.translation.x = (S.zDim/row) * (i)
                p.frame_pos.transform.translation.y = (S.yDim/col) * (j)
                p.frame_pos.transform.translation.z = 0.0
                p.frame_pos.child_frame_id = p.frame_pos.header.frame_id+str(p.frame_pos.transform.translation)
                if (p.frame_pos.transform.translation.x == S.xDim or p.frame_pos.transform.translation.x == 0) != (p.frame_pos.transform.translation.y == S.yDim or p.frame_pos.transform.translation.y == 0):
                    p.edge = True
                if not ((i == row and j == col) or (i == 0 and j == col) or (i == row and j ==0) or (i == 0 and j == 0)):
                    self.points.append(p)

                if i == 0 and not (j == 0 or j == col):
                    gp = Vertice(TransformStamped(),S.surfaceB)
                    gp.frame_pos.header.frame_id = 'surfaceB'
                    gp.frame_pos.header.stamp = rclpy.time.Time().to_msg()
                    gp.id = "%s_%d_%d" %('surfaceBF', i, j)
                    gp.ground = True
                    gp.frame_pos.transform.translation.x = 0.0
                    gp.frame_pos.transform.translation.y = (S.yDim/col) * (j)
                    gp.frame_pos.transform.translation.z = (S.zDim/row)
                    gp.frame_pos.child_frame_id = p.frame_pos.header.frame_id+str(p.frame_pos.transform.translation)
                    self.points.append(gp)

        for i in range(row):
            for j in range(1,col):
                p = Vertice(TransformStamped(),S.surfaceC)
                
                p.frame_pos.header.frame_id = 'surfaceC'
                p.frame_pos.header.stamp = rclpy.time.Time().to_msg()
                p.id = "%s_%d_%d" %('surfaceC', i, j)
                p.frame_pos.transform.translation.x = (S.zDim/row) * (i)
                p.frame_pos.transform.translation.y = (S.yDim/col) * (j)
                p.frame_pos.transform.translation.z = 0.0
                p.frame_pos.child_frame_id = p.frame_pos.header.frame_id+str(p.frame_pos.transform.translation)
                if (p.frame_pos.transform.translation.x == S.xDim or p.frame_pos.transform.translation.x == 0) != (p.frame_pos.transform.translation.y == S.yDim or p.frame_pos.transform.translation.y == 0):
                    p.edge = True
                if not ((i == row and j == col) or (i == 0 and j == col) or (i == row and j ==0) or (i == 0 and j == 0)):
                    self.points.append(p)

                if i == 0 and not (j == 0 or j == col):
                    gp = Vertice(TransformStamped(),S.surfaceC)
                    gp.frame_pos.header.frame_id = 'surfaceC'
                    gp.frame_pos.header.stamp = rclpy.time.Time().to_msg()
                    gp.id = "%s_%d_%d" %('surfaceCF', i, j)
                    gp.ground = True
                    gp.frame_pos.transform.translation.x = 0.0
                    gp.frame_pos.transform.translation.y = (S.yDim/col) * (j)
                    gp.frame_pos.transform.translation.z = (S.zDim/row)
                    gp.frame_pos.child_frame_id = p.frame_pos.header.frame_id+str(p.frame_pos.transform.translation)
                    self.points.append(gp)

        row,col = (6, 2)
        for i in range(row+1):
            for j in range(col+1):
                p = Vertice(TransformStamped(),S.surfaceD)
                p.frame_pos.header.frame_id = 'surfaceD'
                p.frame_pos.header.stamp = rclpy.time.Time().to_msg()
                p.id = "%s_%d_%d" %('surfaceD', i, j)
                p.frame_pos.transform.translation.x = (S.zDim/row) * (i)
                p.frame_pos.transform.translation.y = (S.xDim/col) * (j)
                p.frame_pos.transform.translation.z = 0.0
                p.frame_pos.child_frame_id = p.frame_pos.header.frame_id+str(p.frame_pos.transform.translation)
                if (p.frame_pos.transform.translation.x == S.zDim or p.frame_pos.transform.translation.x == 0) != (p.frame_pos.transform.translation.y == S.xDim or p.frame_pos.transform.translation.y == 0):
                    p.edge = True
                if not ((i == row and j == col) or (i == 0 and j == col) or (i == row and j ==0) or (i == 0 and j == 0)):
                    self.points.append(p)

                if i == 0 and not (j == 0 or j == col):
                    gp = Vertice(TransformStamped(),S.surfaceD)
                    gp.frame_pos.header.frame_id = 'surfaceD'
                    gp.frame_pos.header.stamp = rclpy.time.Time().to_msg()
                    gp.id = "%s_%d_%d" %('surfaceDF', i, j)
                    gp.ground = True
                    gp.frame_pos.transform.translation.x = 0.0
                    gp.frame_pos.transform.translation.y = (S.xDim/col) * (j)
                    gp.frame_pos.transform.translation.z = (S.zDim/row)
                    gp.frame_pos.child_frame_id = p.frame_pos.header.frame_id+str(p.frame_pos.transform.translation)
                    self.points.append(gp)

        # broadcastPoints = []
        # for p in self.points:
        #     broadcastPoints.append(p.frame_pos)

        # self.tfPointStaticBroadcaster.sendTransform(broadcastPoints)

                
        # Transform point from surface frame to base frame and create marker
        for p in self.points:
            vertice = Marker()
            vertice.header.frame_id = p.frame_pos.header.frame_id
            vertice.header.stamp = rclpy.time.Time().to_msg()
            vertice.type = vertice.SPHERE
            vertice.action = vertice.ADD
            vertice.id = self.id
            self.id += 1
            vertice.scale.x = 0.01
            vertice.scale.y = 0.01
            vertice.scale.z = 0.01
            vertice.pose.position.x = p.frame_pos.transform.translation.x
            vertice.pose.position.y = p.frame_pos.transform.translation.y
            vertice.pose.position.z = p.frame_pos.transform.translation.z
            vertice.pose.orientation.x = 0.0
            vertice.pose.orientation.y = 0.0
            vertice.pose.orientation.z = 0.0
            vertice.pose.orientation.w = 1.0
            vertice.color.r = 0.0
            vertice.color.g = 0.0
            vertice.color.b = 0.0
            vertice.color.a = 1.0
            # if p.edge:
            # 	vertice.color.r = 0.5
            # 	vertice.color.g = 0
            # 	vertice.color.b = 1
            # 	vertice.color.a = 1
            verticeArray.markers.append(vertice)
        
        # #create graph	
        # for j in self.points:
        #     print(j.frame_pos.child_frame_id)
            
        #     waiting = True
        #     while waiting:
        #         self.tfPointStaticBroadcaster.sendTransform(j.frame_pos)
        #         # try:
        #         j.pos = self.tfBuffer.lookup_transform(j.frame_pos.child_frame_id, 'odom_frame', rclpy.time.Time())
        #         waiting = False
        #         # except TransformException:
        #             # continue
        #     print(221)
        #     vert=j.id
        #     edges = []
        #     for k in self.points:
        #         a = np.array((j.pos.transform.translation.x, j.pos.transform.translation.y, j.pos.transform.translation.z))
        #         b = np.array((k.pos.transform.translation.x, k.pos.transform.translation.y, k.pos.transform.translation.z))
        #         dist = np.linalg.norm(a-b)
        #         if (not (j.edge and k.edge) and not(j.ground and k.ground) and # ensure edge points cannot connect to edge points and ground points cannont connect to ground points
        #         ((dist < 0.33 and not j.pos == k.pos and j.surface == k.surface and not (j.edge or k.edge or j.ground or k.ground)) or # establish connections on face of surface, excluding edge points and ground points
        #         (dist < 0.245 and j.ground != k.ground and j.surface == k.surface) or # establish connections to ground points
        #         (dist < 0.245 and j.edge != k.edge and j.surface == k.surface) or # establish connections to edge points
        #         (dist < 0.245 and j.edge != k.edge and j.surface != k.surface and (j.surface in S.surfaces[k.surface.id])))): # establish connections between surfaces
        #             edge = F.getEdge(j,k,dist, self.tfBuffer)
        #             edges.append(edge)

        #     self.graph[vert] = edges
        # print('finished graph')

        # # visualize connections between vertices	
        # line = Marker()
        # line.header.frame_id = "odom_frame"
        # line.header.stamp = rclpy.time.Time().to_msg()
        # line.type = vertice.LINE_LIST
        # line.action = vertice.ADD
        # line.id = self.id
        # line.scale.x = 0.005
        # line.pose.orientation.x = 0.0
        # line.pose.orientation.y = 0.0
        # line.pose.orientation.z = 0.0
        # line.pose.orientation.w = 1.0
        # line.color.r = 0.0
        # line.color.g = 0.0
        # line.color.b = 0.0
        # line.color.a = 1.0
            
        # for vert in self.graph:
        #     for nxtvert in self.graph[vert]:
        #         line.points.append(nxtvert.target.pos.transform.translation)
        #         line.points.append(nxtvert.source.pos.transform.translation)

        # # publish markers and listen for new target
        while rclpy.ok():
            self.graphPub.publish(message_converter.convert_dictionary_to_ros_message('std_msgs/msg/String', self.graph))
            self.markerPub.publish(surface)
            self.markerAPub.publish(verticeArray)
            # self.markerPub.publish(line)

def main(args=None):
    rclpy.init(args=args)
    modelTest = ModelTest()
    rclpy.spin(modelTest)

    modelTest.destroy_node()
    rclpy.shutdown()
		
if __name__ == '__main__':
    main()