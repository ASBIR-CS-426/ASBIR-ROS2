#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from _classes import Vertice, FindEdge, Surfaces, Edge
from aStar import AStar
from geometry_msgs.msg import Point, Quaternion, Transform, TransformStamped, Pose, Vector3, PointStamped, PoseStamped
import numpy as np
from nav_msgs.msg import Odometry, Path
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from rclpy_message_converter import message_converter

class BestPath(Node):
    def __init__(self):
            super().__init__('PotentialField')
            self.pathPub = self.create_publisher(Path, 'path', 1)
            self.targetSub = self.create_subscription(PointStamped, 'targetPoint', self.buildPath, 10)
            self.graphSub = self.create_subscription(PointStamped, 'targetPoint', self.graphCallback, 10)
            self.tfBuffer = Buffer()
            self.tfListener = TransformListener(self.tfBuffer, self)

            self.path = Path()
            self.graph = None

    def graphCallback(self, msg):
        self.graph = message_converter.convert_ros_message_to_dictionary(msg)

    def getRobotPose(self):
        return self.tfBuffer.lookup_transform('camera_pose_frame','camera_odom_frame', rclpy.time.Time())

    def buildPath(self, msg):
        if self.graph == None:
            self.get_logger().info('Abort BuildPath: graph == None')
            return
        currentPose = self.getRobotPose()
        findPath = AStar()

        # set starting vertice to current position of robot
        start = Vertice()
        start.pos.point = Point(currentPose.transform.translation.x, currentPose.transform.translation.y, currentPose.transform.translation.z - 0.19)
        start.id = 'start'
        start.pos.header.frame_id = 'camera_odom_frame'

    	# set goal vertice to Target message
        end = Vertice()
        end.pos.point = msg
        end.pos.point.z = end.pos.point.z - 0.19
        end.pos.header.frame_id = 'camera_odom_frame'
        end.id = 'end'

        start_ = np.array((start.pos.point.x, start.pos.point.y, start.pos.point.z))
        endA = np.array((end.pos.point.x, end.pos.point.y, end.pos.point.z))
        mindS = 500
        mindE = 500
        minS = Vertice()
        minS.pos.point = Point(500,500,500)
        minE = Vertice()
        minE.pos.point = Point(500,500,500)
    
        # find nodes closest to start and end
        for i in points:
            a = np.array((i.pos.point.x,i.pos.point.y,i.pos.point.z))
            distS = np.linalg.norm(start_ - a)
            distE = np.linalg.norm(endA - a)
            if distS < mindS:
                mindS = distS
                minS = i
            if distE < mindE:
                mindE = distE
                minE = i

# 	# find neighbor of node closest to goal that is closest to the starting position
# 	targetNode = minE
# 	for node in verticeGraph[minE.id]:
# 		targetNodeA = np.array((targetNode.pos.point.x, targetNode.pos.point.y, targetNode.pos.point.z))
# 		targetNodeD = np.linalg.norm(startA - targetNodeA)
# 		nodeA = np.array((node.target.pos.point.x, node.target.pos.point.y, node.target.pos.point.z))
# 		nodeD = np.linalg.norm(startA - nodeA)
# 		if nodeD < targetNodeD and node.target.surface == start.surface:
# 			targetNode = node.target

# 	sEdge = Edge(start,minS,mindS,current_pose.transform.rotation)
# 	verticeGraph[start.id] = [sEdge]

# 	# find path from start to end, return list of node ids and dictionary of path edges using node ids as keys
# 	pathNodes, pathEdges = findPath.aStar(verticeGraph, start.id, targetNode.id)

# 	# visualize path
# 	path = Marker()
# 	# path.header.frame_id = "robot_odom_frame"
# 	path.header.frame_id = "camera_odom_frame"
# 	path.header.stamp = rospy.get_rostime()
# 	path.type = path.LINE_LIST
# 	path.action = path.ADD
# 	id += 1
# 	path.id = id
# 	path.scale.x = 0.01
# 	path.pose.orientation.x = 0.0
# 	path.pose.orientation.y = 0.0
# 	path.pose.orientation.z = 0.0
# 	path.pose.orientation.w = 1.0
# 	path.color.r = 1
# 	path.color.g = 1
# 	path.color.b = 0
# 	path.color.a = 1

# 	pathPoints = Path()

# 	# find transformation from starting pose to the first waypoint
# 	st = findStartTransform(minS, start, tfBuffer)
# 	pathPoints.path.append(st)
# 	path.points.append(start.pos.point)
# 	path.points.append(minS.pos.point)

# 	end_frame_id = 0
# 	# create transforms from waypoint to waypoint
# 	for i in range(2,len(pathNodes)):
# 		path.points.append(pathEdges[pathNodes[i]].source.pos.point)
# 		path.points.append(pathEdges[pathNodes[i]].target.pos.point)
# 		t = TransformStamped()
# 		t.transform = Transform(Vector3(pathEdges[pathNodes[i]].target.pos.point.x, pathEdges[pathNodes[i]].target.pos.point.y, pathEdges[pathNodes[i]].target.pos.point.z), 
# 										pathEdges[pathNodes[i]].rotation)
# 		# t.header.frame_id = 'robot_odom_frame'		
# 		t.header.frame_id = 'camera_odom_frame'
# 		t.child_frame_id = str(i)
# 		pathPoints.path.append(t)
# 		end_frame_id = i+1

# 	# find transform from final node to the end goal
# 	et = findEndTransform(end, targetNode, tfBuffer, end_frame_id)
# 	pathPoints.path.append(et)
# 	path.points.append(targetNode.pos.point)
# 	path.points.append(end.pos.point)
	
# 	# publish transform array and visualizations
# 	broadcaster.sendTransform(pathPoints.path)
# 	path_pub.publish(pathPoints)
# 	vis_pub.publish(path)