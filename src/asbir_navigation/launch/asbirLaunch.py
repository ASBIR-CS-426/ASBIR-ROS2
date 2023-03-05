from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    realsense2_dir = get_package_share_directory('realsense2_camera')
    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2'
        ),
        Node(
            package='asbir_navigation',
            executable='modelTest',
            name='model'
        ),
        Node(
            package='asbir_navigation',
            executable='graphTest',
            name='graph'
        ),
        Node(
            package='asbir_navigation',
            executable='buildBestPath',
            name='buildPath',
        ),
        Node(
            package='asbir_navigation',
            executable='pathController',
            name='path',
        ),
        Node(
            package='asbir_navigation',
            executable='potentialField',
            name='potentialField',
        ),
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(
        #         realsense2_dir + '/launch/rs_d400_and_t265_launch.py'),
        #     launch_arguments={
        #         'enable_pointcloud': 'true',
        #     })
    ])