from launch import LaunchDescription
from launch_ros.actions import Node
import launch
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    realsense2_dir = get_package_share_directory('realsense2_camera')
    included_launch = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
                realsense2_dir + '/launch/rs_d400_and_t265_launch.py'))
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
        included_launch
    ])