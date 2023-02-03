#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from asbir_navigation.classes import *
from asbir_navigation.aStar import AStar
from geometry_msgs.msg import Point, Quaternion, PointStamped, Transform
from visualization_msgs.msg import Marker
import numpy as np
from nav_msgs.msg import Path
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_ros.transform_broadcaster import TransformBroadcaster
from parse import *
from rclpy.duration import Duration
from asbir_navigation import *

class BestPath(Node):
    def __init__(self):
            super().__init__('BuildBestPath')
            self.pathPub = self.create_publisher(Path, 'path', 1)
            self.visPub = self.create_publisher(Marker, "visualization_marker", 10)
            self.targetSub = self.create_subscription(PointStamped, 'targetPoint', self.buildPath, 10)
            self.tfBuffer = Buffer()
            self.tfListener = TransformListener(self.tfBuffer, self)
            self.tfBroadcaster = TransformBroadcaster(self)
            self.graph = {}

            self.loadGraph()

    def loadGraph(self):
        S=Surfaces()
        lines = None
        edges = []
        id=''
        with open("src/asbir_navigation/graphs/mapGraph.txt", "r") as f: 
            lines = f.readlines()
        for line in lines:
            if ':' in line:
                try:
                    print(edges[0].source.pos.point.x,edges[0].source.pos.point.y,edges[0].source.pos.point.z)
                    self.graph[id] = edges
                    edges=[]
                except (UnboundLocalError, IndexError):
                    pass
                id = search("{}:", line).fixed[0]
                self.graph[id]=[]
                
            else:
                parsed=search('-source=(id={}, frame_pos=geometry_msgs.msg.PointStamped(header=std_msgs.msg.Header(stamp=builtin_interfaces.msg.Time(sec=0, nanosec=0), frame_id=\'{}\'), point=geometry_msgs.msg.Point(x={}, y={}, z={})), surface={}, edge={}, ground={}, pos=geometry_msgs.msg.PointStamped(header=std_msgs.msg.Header(stamp=builtin_interfaces.msg.Time(sec=0, nanosec=0), frame_id=\'{}\'), point=geometry_msgs.msg.Point(x={}, y={}, z={}))) ,target=(id={}, frame_pos=geometry_msgs.msg.PointStamped(header=std_msgs.msg.Header(stamp=builtin_interfaces.msg.Time(sec=0, nanosec=0), frame_id=\'{}\'), point=geometry_msgs.msg.Point(x={}, y={}, z={})), surface={}, edge={}, ground={}, pos=geometry_msgs.msg.PointStamped(header=std_msgs.msg.Header(stamp=builtin_interfaces.msg.Time(sec=0, nanosec=0), frame_id=\'{}\'), point=geometry_msgs.msg.Point(x={}, y={}, z={}))) ,distance={},rotation=geometry_msgs.msg.Quaternion(x={}, y={}, z={}, w={})',line).fixed
                print(parsed[9],parsed[10],parsed[11])
                source=Vertice(id=parsed[0],surface=S.surface[parsed[5]],edge=bool(parsed[6]),ground=bool(parsed[7]))
                source.frame_pos.header.frame_id=parsed[1]
                source.frame_pos.point=Point(x=float(parsed[2]),y=float(parsed[3]),z=float(parsed[4]))
                source.pos.header.frame_id=parsed[8]
                source.pos.point=Point(x=float(parsed[9]),y=float(parsed[10]),z=float(parsed[11]))

                target=Vertice(id=parsed[12],surface=S.surface[parsed[17]],edge=parsed[18],ground=parsed[19])
                target.frame_pos.header.frame_id=parsed[6]
                target.frame_pos.point=Point(x=float(parsed[14]),y=float(parsed[15]),z=float(parsed[16]))
                target.pos.header.frame_id=parsed[20]
                target.pos.point=Point(x=float(parsed[21]),y=float(parsed[22]),z=float(parsed[23]))
                
                distance=float(parsed[24])
                rotation=Quaternion(x=float(parsed[25]),y=float(parsed[26]),z=float(parsed[27]),w=float(parsed[28]))

                self.graph[id].append(Edge(source, target, distance, rotation))
                # print(str(Edge(source, target, distance, rotation)))
                # print(source.id,target.id)

        # for key in self.graph:
        #     try:
        #         print(self.graph[key][0].source.pos.point.x, self.graph[key][0].source.pos.point.y, self.graph[key][0].source.pos.point.z)
        #         # print(self.graph[key][0].target.pos.point.x, self.graph[key][0].target.pos.point.y, self.graph[key][0].target.pos.point.z)
        #     except IndexError:
        #         continue

    def findEndTransform(end, targetNode, tfBuffer, frame_id):
        # if target node is not on the ground use the frame of its surface, otherwise use base frame
        if not targetNode.ground:
            end_frame_pos = tfBuffer.transform(end.pos, targetNode.surface.id)
            target_frame_pos = targetNode.frame_pos
        else:
            end_frame_pos = end.pos
            target_frame_pos = targetNode.pos

        endA = np.array((end_frame_pos.point.x, end_frame_pos.point.y, end_frame_pos.point.z))
        targetNodeA = np.array((target_frame_pos.point.x, target_frame_pos.point.y, target_frame_pos.point.z))
        # find distance vector between start and node
        ed = endA - targetNodeA
        # find angle between target node and end, relative to the set frame
        e_yaw = np.arctan2(ed[1],ed[0])
        # create z and w values for rotation quaternion
        ez = np.sin(e_yaw/2)
        ew = np.cos(e_yaw/2)
        e = PoseStamped()
        e.pose = Pose(end.pos.point, Quaternion(0,0,ez,ew))
        e.header.frame_id = targetNode.surface.id
        # transform pose into the base frame
        # e = tfBuffer.transform(e, 'robot_odom_frame', rospy.Duration(10))
        e = tfBuffer.transform(e, 'odom_frame', Duration(10))
        et = TransformStamped()
        et.transform.translation = Vector3(end.pos.point.x, end.pos.point.y, end.pos.point.z)
        et.transform.rotation = e.pose.orientation
        # et.header.frame_id = 'robot_odom_frame'
        et.header.frame_id = 'odom_frame'
        et.child_frame_id = str(frame_id)
        return et

    def findStartTransform(start, minS, tfBuffer):
        # if starting node is not on the ground use the frame of its surface, otherwise use base frame
        if not minS.ground:
            start_frame_pos = tfBuffer.transform(start.pos, minS.surface.id)
            minS_frame_pos = minS.frame_pos
        else:
            start_frame_pos = start.pos
            minS_frame_pos = minS.pos 

        startA = np.array((start_frame_pos.point.x, start_frame_pos.point.y, start_frame_pos.point.z))
        minSA = np.array((minS_frame_pos.point.x, minS_frame_pos.point.y, minS_frame_pos.point.z))
        # find distance vector between start and node
        sd = startA - minSA
        # find angle between start and node, relative to the set frame
        s_yaw = np.arctan2(sd[1],sd[0])
        # create z and w values for rotation quaternion
        sz = np.sin(s_yaw/2)
        sw = np.cos(s_yaw/2)
        s = PoseStamped()
        s.pose = Pose(start.pos.point, Quaternion(0,0,sz,sw))
        s.header.frame_id = minS.surface.id
        # transform pose into the base frame
        # s = tfBuffer.transform(s, 'robot_odom_frame', rospy.Duration(10))
        s = tfBuffer.transform(s, 'odom_frame', Duration(10))
        st = TransformStamped()
        st.transform.translation = Vector3(start.pos.point.x, start.pos.point.y, start.pos.point.z)
        st.transform.rotation = s.pose.orientation
        # st.header.frame_id = 'robot_odom_frame'
        st.header.frame_id = 'odom_frame'
        st.child_frame_id = '1'
        return st
    
    def getRobotPose(self):
        return self.tfBuffer.lookup_transform('T265_pose_frame','odom_frame', rclpy.time.Time(), timeout = Duration(seconds=1))

    def buildPath(self, msg):
        if self.graph == None:
            self.get_logger().info('Abort BuildPath: graph == None')
            return
        currentPose = self.getRobotPose()
        findPath = AStar()

        # set starting vertice to current position of robot
        start = Vertice()
        start.pos.point = Point(x=currentPose.transform.translation.x, y=currentPose.transform.translation.y, z=currentPose.transform.translation.z - 0.19)
        start.id = 'start'
        start.pos.header.frame_id = 'odom_frame'

    	# set goal vertice to Target message
        end = Vertice()
        end.pos = msg
        end.pos.point.z = end.pos.point.z - 0.19
        end.pos.header.frame_id = 'odom_frame'
        end.id = 'end'

        startA = np.array((start.pos.point.x, start.pos.point.y, start.pos.point.z))
        endA = np.array((end.pos.point.x, end.pos.point.y, end.pos.point.z))
        mindS = 500
        mindE = 500
        minS = Vertice()
        minS.pos.point = Point(x=500.0,y=500.0,z=500.0)
        minE = Vertice()
        minE.pos.point = Point(x=500.0,y=500.0,z=500.0)
    
        # find nodes closest to start and end
        for i in self.graph:
            try:
                a = np.array((self.graph[i][0].source.pos.point.x,self.graph[i][0].source.pos.point.y,self.graph[i][0].source.pos.point.z))
                distS = np.linalg.norm(startA - a)
                distE = np.linalg.norm(endA - a)
                # print(a)
                # print(distS)
                # print(distE)
                # print('\n')
                if distS < mindS:
                    mindS = distS
                    minS = i
                if distE < mindE:
                    mindE = distE
                    minE = i
            except IndexError:
                continue

        # find neighbor of node closest to goal that is closest to the starting position
        targetNode = minE
        for node in self.graph[minE.id]:
            targetNodeA = np.array((targetNode.pos.point.x, targetNode.pos.point.y, targetNode.pos.point.z))
            targetNodeD = np.linalg.norm(startA - targetNodeA)
            nodeA = np.array((node.target.pos.point.x, node.target.pos.point.y, node.target.pos.point.z))
            nodeD = np.linalg.norm(startA - nodeA)
            if nodeD < targetNodeD and node.target.surface == start.surface:
                targetNode = node.target

        sEdge = Edge(start,minS,mindS,currentPose.transform.rotation)
        self.graph[start.id] = [sEdge]

        # find path from start to end, return list of node ids and dictionary of path edges using node ids as keys
        pathNodes, pathEdges = findPath.aStar(self.graph, start.id, targetNode.id)

        # visualize path
        path = Marker()
        # path.header.frame_id = "robot_odom_frame"
        path.header.frame_id = "odom_frame"
        path.header.stamp = self.get_clock().now().to_msg()
        path.type = path.LINE_LIST
        path.action = path.ADD
        id += 1
        path.id = id
        path.scale.x = 0.01
        path.pose.orientation.x = 0.0
        path.pose.orientation.y = 0.0
        path.pose.orientation.z = 0.0
        path.pose.orientation.w = 1.0
        path.color.r = 1
        path.color.g = 1
        path.color.b = 0
        path.color.a = 1

        pathPoints = Path()

        # find transformation from starting pose to the first waypoint
        st = self.findStartTransform(minS, start, self.tfBuffer)
        pathPoints.path.append(st)
        path.points.append(start.pos.point)
        path.points.append(minS.pos.point)

        end_frame_id = 0
        # create transforms from waypoint to waypoint
        for i in range(2,len(pathNodes)):
            path.points.append(pathEdges[pathNodes[i]].source.pos.point)
            path.points.append(pathEdges[pathNodes[i]].target.pos.point)
            t = TransformStamped()
            t.transform = Transform(Vector3(pathEdges[pathNodes[i]].target.pos.point.x, pathEdges[pathNodes[i]].target.pos.point.y, pathEdges[pathNodes[i]].target.pos.point.z), 
                                            pathEdges[pathNodes[i]].rotation)
            # t.header.frame_id = 'robot_odom_frame'		
            t.header.frame_id = 'camera_odom_frame'
            t.child_frame_id = str(i)
            pathPoints.path.append(t)
            end_frame_id = i+1

        # find transform from final node to the end goal
        et = self.findEndTransform(end, targetNode, self.tfBuffer, end_frame_id)
        pathPoints.path.append(et)
        path.points.append(targetNode.pos.point)
        path.points.append(end.pos.point)
        
        # publish transform array and visualizations
        self.tfBroadcaster.sendTransform(pathPoints.path)
        self.pathPub.publish(pathPoints)
        self.visPub.publish(path)

def main(args=None):
    rclpy.init(args=args)
    node = BestPath()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()