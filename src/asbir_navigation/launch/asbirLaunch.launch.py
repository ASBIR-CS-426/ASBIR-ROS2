from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node
from launch.actions import TimerAction

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    realsense2_dir = get_package_share_directory('realsense2_camera')
    apriltag_dir = get_package_share_directory('apriltag_ros')
    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                apriltag_dir + '/launch/tag_realsense.launch.py'),
        ),
        Node(
            package = "tf2_ros",
            executable = "static_transform_publisher",
            arguments = ["0.0073", "0.0242", "0.0089", "0.0", "0.523598776", "0.0", "T265_pose_frame", "D400_link"]
        ),
        TimerAction(
            period=2.0,
            actions=[
                Node(
                    package='asbir_navigation',
                    executable='ModelTest',
                    name='Model'
                ),
            ]
        ),
        TimerAction(
            period=3.0,
            actions=[
                Node(
                    package='asbir_navigation',
                    executable='GraphTest',
                    name='Graph'
                ),
            ]  
        ),
        Node(
            package='asbir_navigation',
            executable='BuildBestPath',
            name='BuildPath',
        ),
        Node(
            package='asbir_navigation',
            executable='PathController',
            name='PathController',
        ),
        Node(
            package='asbir_navigation',
            executable='PotentialField',
            name='PotentialField',
        ),
        
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(
        #         realsense2_dir + '/launch/rs_d400_and_t265_launch.py'),
        #     ),
        
    ])

# python3 src/realsense/realsense2_camera/scripts/set_cams_transforms.py T265_link D400_link 0.0073 0.0242 0.0089 -30 0 0