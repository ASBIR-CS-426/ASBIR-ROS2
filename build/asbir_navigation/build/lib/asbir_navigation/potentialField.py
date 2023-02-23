#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, Bool, String
from geometry_msgs.msg import Pose, TransformStamped, Transform
import numpy as np
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from .transformations import *

class PotentialField(Node):
    def __init__(self):
        super().__init__('PotentialField')
        self.servoControlPub = self.create_publisher(Float32MultiArray, 'servoControl', 1)
        self.waypointReachedPub = self.create_publisher(Bool, 'waypointReached', 1)
        self.transformPub = self.create_publisher(Transform, 'transformToWaypoint', 1)

        # self.staticTransformBroadCaster = StaticTransformBroadcaster()
        self.tfBuffer = Buffer()
        self.tfListener = TransformListener(self.tfBuffer, self)

        self.vr_max = 0.25
        self.vr = 0
        self.wheel_rotation_max = np.pi/2
        self.reachDist = 0.1
        self.reached = Bool()
        self.activePath=False

        self.activePathSub=self.create_subscription(Bool, 'activePath', self.activeCallback, 10)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)     

    def activeCallback(self, msg):
        self.activePath=msg.data

    def broadcast_timer_callback(self):
        if self.activePath:
            self.reached.data = False
            waypoint = TransformStamped()
            try:
                waypoint=self.tfBuffer.lookup_transform('waypoint', 'T265_pose_frame', rclpy.time.Time())
                print(waypoint.transform.translation.x, waypoint.transform.translation.y, waypoint.transform.translation.z)
            except TransformException as ex:
                print('Could not transform T265_pose_frame to waypoint', ex)
                return


            # Find normal distance between robot and waypoint
            dist = np.linalg.norm([waypoint.transform.translation.x, waypoint.transform.translation.y, waypoint.transform.translation.z])
            # Convert quaternion to euler
            roll, pitch, yaw = euler_from_quaternion(waypoint.transform.rotation)

            print("Transform Rotation: ", roll, pitch, yaw)
            print("Transform Translation: ", waypoint.transform.translation.x, waypoint.transform.translation.y, waypoint.transform.translation.z)

            # # set velocity controller of robot
            vr = self.vr_max

            # limit maximum rotation (correcting for +/- angles)
            if yaw > 0:
                wheel_rotation = np.minimum(yaw, self.wheel_rotation_max)
            elif yaw < 0:
                wheel_rotation = np.maximum(yaw, -self.wheel_rotation_max)

            # Iterate to next waypoint if within reach radius of waypoint
            if(dist < self.reachDist):
                wheel_rotation = 0
                vr = 0
                self.reached.data = True


            # convert control values to servo value range 
                # Steering 1500 = 0, 900 - 2100
                # Wheel rotation 1600 = 0, 800 - 2400
            fs = float(wheel_rotation / self.wheel_rotation_max)
            bs = float(wheel_rotation / self.wheel_rotation_max)
            fw = float(vr)
            bw = float(vr)

            servoControl = Float32MultiArray()
            servoControl.data = [fs,bs,fw,bw]
            self.waypointReachedPub.publish(self.reached)
            self.servoControlPub.publish(servoControl)
            self.transformPub.publish(waypoint.transform)
        
def main(args=None):
    rclpy.init(args=args)
    node = PotentialField()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()