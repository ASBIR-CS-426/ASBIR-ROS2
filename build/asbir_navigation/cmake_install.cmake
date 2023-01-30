# Install script for directory: /home/aralab/ASBIR-ROS2/src/asbir_navigation

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/aralab/ASBIR-ROS2/install/asbir_navigation")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation/listener" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation/listener")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation/listener"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation" TYPE EXECUTABLE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/listener")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation/listener" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation/listener")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation/listener"
         OLD_RPATH "/home/aralab/ros2_foxy/install/rclcpp/lib:/home/aralab/ros2_foxy/install/libstatistics_collector/lib:/home/aralab/ros2_foxy/install/std_msgs/lib:/home/aralab/ros2_foxy/install/rcl/lib:/home/aralab/ros2_foxy/install/rcl_interfaces/lib:/home/aralab/ros2_foxy/install/rmw_implementation/lib:/home/aralab/ros2_foxy/install/rmw/lib:/home/aralab/ros2_foxy/install/rcl_logging_spdlog/lib:/home/aralab/ros2_foxy/install/rcl_yaml_param_parser/lib:/home/aralab/ros2_foxy/install/libyaml_vendor/lib:/home/aralab/ros2_foxy/install/rosgraph_msgs/lib:/home/aralab/ros2_foxy/install/statistics_msgs/lib:/home/aralab/ros2_foxy/install/builtin_interfaces/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_c/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_c/lib:/home/aralab/ros2_foxy/install/rcpputils/lib:/home/aralab/ros2_foxy/install/rosidl_runtime_c/lib:/home/aralab/ros2_foxy/install/rcutils/lib:/home/aralab/ros2_foxy/install/tracetools/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation/listener")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation/environment" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/pythonpath.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation/environment" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/pythonpath.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.8/site-packages/asbir_navigation" TYPE DIRECTORY FILES "/home/aralab/ASBIR-ROS2/src/asbir_navigation/asbir_navigation/" REGEX "/[^/]*\\.pyc$" EXCLUDE REGEX "/\\_\\_pycache\\_\\_$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(
        COMMAND
        "/usr/bin/python3" "-m" "compileall"
        "/home/aralab/ASBIR-ROS2/install/asbir_navigation/lib/python3.8/site-packages/asbir_navigation"
      )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/asbir_navigation" TYPE PROGRAM FILES
    "/home/aralab/ASBIR-ROS2/src/asbir_navigation/scripts/publisher_member_function.py"
    "/home/aralab/ASBIR-ROS2/src/asbir_navigation/scripts/modelTest.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/asbir_navigation")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/asbir_navigation")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation/environment" TYPE FILE FILES "/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation/environment" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation/environment" TYPE FILE FILES "/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation/environment" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/local_setup.bash")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/local_setup.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_environment_hooks/package.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_index/share/ament_index/resource_index/packages/asbir_navigation")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation/cmake" TYPE FILE FILES
    "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_core/asbir_navigationConfig.cmake"
    "/home/aralab/ASBIR-ROS2/build/asbir_navigation/ament_cmake_core/asbir_navigationConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/asbir_navigation" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/src/asbir_navigation/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/aralab/ASBIR-ROS2/build/asbir_navigation/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
