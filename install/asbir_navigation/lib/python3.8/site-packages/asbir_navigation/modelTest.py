#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Quaternion, TransformStamped, PoseStamped, Vector3, Transform
from tf2_ros.transform_broadcaster import TransformBroadcaster
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from asbir_navigation.classes import *
import numpy as np
import tf2_ros
from .transformations import *
import tf2_geometry_msgs.tf2_geometry_msgs 

class ModelTest(Node):
    def __init__(self):
        super().__init__('Model')
        self.markerPub = self.create_publisher(
            Marker, 
            "visualization_marker", 
            10)
        self.tfBroadcaster = TransformBroadcaster(self)
        self.tfBuffer = Buffer()
        self.tfListener = TransformListener(self.tfBuffer, self)
        # self.structureFrame = TransformStamped()
        # self.aligned = False

        # self.align_apriltag_timer = self.create_timer(0.1, self.align_apriltag)
        self.timer = self.create_timer(0.4, self.broadcast_timer_callback)     

    # def align_apriltag(self):
    #     if self.aligned:
    #         return
    #     try:
    #         self.structureFrame = self.tfBuffer.lookup_transform("odom_frame", "tag16h5:2", time=rclpy.time.Time())
    #         self.aligned = True
    #     except (tf2_ros.LookupException, tf2_ros.ExtrapolationException):
    #          i =0


    def broadcast_timer_callback(self):
        # if not self.aligned:
        #     return
        # wait until april tag is detected     
        S = Surfaces()
        
        
        #====Build Structure Model===
        # Create base surface model
        structureModel=Marker()
        structureModel.header.frame_id = "structure"
        structureModel.header.stamp = rclpy.time.Time().to_msg()
        structureModel.ns = "Namespace"
        structureModel.id = 0
        structureModel.type = structureModel.CUBE
        structureModel.action = structureModel.ADD
        structureModel.scale.x = S.xDim
        structureModel.scale.y = S.yDim
        structureModel.scale.z = S.zDim
        structureModel.pose.position.x = -S.xDim/2 #+ S.xOffset)
        structureModel.pose.position.y = -(S.yDim/2 + S.yOffset)
        structureModel.pose.position.z = S.zDim/2 #+ S.zOffset
        structureModel.pose.orientation.x = 0.0
        structureModel.pose.orientation.y = 0.0
        structureModel.pose.orientation.z = 0.0
        structureModel.pose.orientation.w = 1.0
        structureModel.color.r = 0.5
        structureModel.color.g = 0.5
        structureModel.color.b = 0.5
        structureModel.color.a = 1.0

        self.markerPub.publish(structureModel)
        self.tfBroadcaster.sendTransform([
                            S.surfaceA.frame, 
                            S.surfaceB.frame,
                            S.surfaceC.frame,
                            S.surfaceD.frame])

def main(args=None):
    rclpy.init(args=args)
    node = ModelTest()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
   