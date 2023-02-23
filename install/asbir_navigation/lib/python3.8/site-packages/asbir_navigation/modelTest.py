#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Quaternion
from tf2_ros.transform_broadcaster import TransformBroadcaster

from asbir_navigation.classes import *

class ModelTest(Node):
    def __init__(self):
        super().__init__('Model')
        self.markerPub = self.create_publisher(
            Marker, 
            "visualization_marker", 
            10)
        self.tfBroadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(1, self.broadcast_timer_callback)     
         

    def broadcast_timer_callback(self):
        S = Surfaces()
        #====Build Structure Model===
        # Create base surface model
        surface=Marker()
        surface.header.frame_id = "T265_odom_frame"
        surface.header.stamp = self.get_clock().now().to_msg()
        surface.ns = "Namespace"
        surface.id = 0
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
        

        self.markerPub.publish(surface)
        # broadcast frames of surface
        self.tfBroadcaster.sendTransform([S.surfaceA.frame, 
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
   