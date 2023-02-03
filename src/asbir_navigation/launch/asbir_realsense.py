# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Launch realsense2_camera node without rviz2."""
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import ThisLaunchFileDir
from launch.launch_description_sources import PythonLaunchDescriptionSource
import sys
import pathlib
import importlib.util
import sys
spec = importlib.util.spec_from_file_location("rs_launch.py", "~/ros2_foxy/src/realsense-ros/realsense_camera/launch/rs_launch")
rs_launch = importlib.util.module_from_spec(spec)
sys.modules["rs_launch.py"] = rs_launch
spec.loader.exec_module(rs_launch)
sys.path.append(str(pathlib.Path(__file__).parent.absolute()))


local_parameters = [{'name': 'camera_name1', 'default': 'D435i', 'description': 'camera unique name'},
                    {'name': 'device_type1', 'default': 'd435i.', 'description': 'choose device by type'},
                    {'name': 'camera_name2', 'default': 'T265', 'description': 'camera unique name'},
                    {'name': 'device_type2', 'default': 't265', 'description': 'choose device by type'},
                    {'name': 'enable_fisheye12', 'default': 'false', 'description': 'topic for T265 wheel odometry'},
                    {'name': 'enable_fisheye22', 'default': 'false', 'description': 'topic for T265 wheel odometry'},
                    {'name': 'pointcloud.enable', 'default': 'false', 'description': ''}, 
                    {'name': 'align_depth.enable', 'default': 'false', 'description': ''}, 
                   ]

def generate_launch_description():
    return LaunchDescription(
        rs_launch.declare_configurable_parameters(local_parameters) + 
        [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/asbir_realsense.py']),
            launch_arguments=rs_launch.set_configurable_parameters(local_parameters).items(),
        ),
    ])
