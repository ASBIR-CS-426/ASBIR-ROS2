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
            executable='ModelTest',
            name='Model'
        ),
        Node(
            package='asbir_navigation',
            executable='GraphTest',
            name='Graph'
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
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                realsense2_dir + '/launch/rs_d400_and_t265_launch.py'),
            ),
        Node(
            package = "tf2_ros",
            executable = "static_transform_publisher",
            arguments = ["0.0073", "0.0242", "0.0089", "0.0", "0.523598776", "0.0", "T265_link", "D400_link"]
        ),
        
    ])

# python3 src/realsense/realsense2_camera/scripts/set_cams_transforms.py T265_link D400_link 0.0073 0.0242 0.0089 -30 0 0