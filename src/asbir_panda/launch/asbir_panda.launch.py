from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node
from launch.actions import TimerAction
from ament_index_python.packages import get_package_share_directory

import importlib.util
import sys

realsense2_dir = get_package_share_directory('realsense2_camera')
apriltag_dir = get_package_share_directory('apriltag_ros')


def generate_launch_description():
    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                realsense2_dir + '/launch/rs_d400_and_t265_launch.py'
            ),
            launch_arguments={
                'depth_module.profile': '848,480,15',
                'rgb_camera.profile': '1280,720,15',
            }.items()
        ),        
        Node(
            package = "tf2_ros",
            executable = "static_transform_publisher",
            arguments = ["0.0073", "0.0242", "0.0089", 
                         "0.0", "0.523598776", "0.0", 
                         "T265_pose_frame", "D400_link"]
        ),
        Node(
            package = "tf2_ros",
            executable = "static_transform_publisher",
            arguments = ["-0.00026584944387789643", "0.014810418177772683", "0.0000521025998394935", 
                         "0.029402", "0.0042276", "0.0073457", 
                         "D400_link", "D400_color_frame"]
        ),
        Node(
            package = "tf2_ros",
            executable = "static_transform_publisher",
            arguments = ["0.0", "0.0", "0.0", 
                         "1.5707963", "0.0", "1.5707963", 
                         "D400_color_frame", "D400_color_optical_frame"]
        ),
        Node(
            package = "tf2_ros",
            executable = "static_transform_publisher",
            arguments = ["0.0", "0.0", "0.0", 
                         "1.5707963", "0.0", "1.5707963", 
                         "D400_link", "D400_depth_frame"]
        ),
        Node(
            package = "tf2_ros",
            executable = "static_transform_publisher",
            arguments = ["0.0", "0.0", "0.0", 
                         "1.5707963", "0.0", "1.5707963", 
                         "D400_depth_frame", "D400_depth_optical_frame"]
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                apriltag_dir + '/launch/tag_realsense.launch.py'),
        ),
        Node(
            package = "asbir_panda",
            executable = "AlignAprilTag",
            name = 'AlignAprilTag'
        ),
        Node(
            package = "asbir_serial",
            executable = "serialComm"
        ),
        
    ])
