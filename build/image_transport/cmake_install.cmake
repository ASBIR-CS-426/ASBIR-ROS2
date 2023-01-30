# Install script for directory: /home/aralab/ASBIR-ROS2/src/image_common/image_transport

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/aralab/ASBIR-ROS2/install/image_transport")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/src/image_common/image_transport/default_plugins.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/aralab/ASBIR-ROS2/build/image_transport/libimage_transport.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport.so"
         OLD_RPATH "/home/aralab/ros2_foxy/install/message_filters/lib:/home/aralab/ros2_foxy/install/rclcpp/lib:/home/aralab/ros2_foxy/install/sensor_msgs/lib:/home/aralab/ros2_foxy/install/libstatistics_collector/lib:/home/aralab/ros2_foxy/install/rcl/lib:/home/aralab/ros2_foxy/install/rcl_interfaces/lib:/home/aralab/ros2_foxy/install/rmw_implementation/lib:/home/aralab/ros2_foxy/install/rmw/lib:/home/aralab/ros2_foxy/install/rcl_logging_spdlog/lib:/home/aralab/ros2_foxy/install/rcl_yaml_param_parser/lib:/home/aralab/ros2_foxy/install/libyaml_vendor/lib:/home/aralab/ros2_foxy/install/rosgraph_msgs/lib:/home/aralab/ros2_foxy/install/statistics_msgs/lib:/home/aralab/ros2_foxy/install/tracetools/lib:/home/aralab/ros2_foxy/install/ament_index_cpp/lib:/home/aralab/ros2_foxy/install/class_loader/lib:/home/aralab/ros2_foxy/install/console_bridge_vendor/lib:/home/aralab/ros2_foxy/install/geometry_msgs/lib:/home/aralab/ros2_foxy/install/std_msgs/lib:/home/aralab/ros2_foxy/install/builtin_interfaces/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_c/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_c/lib:/home/aralab/ros2_foxy/install/rcpputils/lib:/home/aralab/ros2_foxy/install/rosidl_runtime_c/lib:/home/aralab/ros2_foxy/install/rcutils/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport_plugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport_plugins.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport_plugins.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/aralab/ASBIR-ROS2/build/image_transport/libimage_transport_plugins.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport_plugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport_plugins.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport_plugins.so"
         OLD_RPATH "/home/aralab/ASBIR-ROS2/build/image_transport:/home/aralab/ros2_foxy/install/message_filters/lib:/home/aralab/ros2_foxy/install/ament_index_cpp/lib:/home/aralab/ros2_foxy/install/class_loader/lib:/home/aralab/ros2_foxy/install/console_bridge_vendor/lib:/home/aralab/ros2_foxy/install/rclcpp/lib:/home/aralab/ros2_foxy/install/libstatistics_collector/lib:/home/aralab/ros2_foxy/install/rcl/lib:/home/aralab/ros2_foxy/install/rcl_interfaces/lib:/home/aralab/ros2_foxy/install/rmw_implementation/lib:/home/aralab/ros2_foxy/install/rmw/lib:/home/aralab/ros2_foxy/install/rcl_logging_spdlog/lib:/home/aralab/ros2_foxy/install/rcl_yaml_param_parser/lib:/home/aralab/ros2_foxy/install/libyaml_vendor/lib:/home/aralab/ros2_foxy/install/rosgraph_msgs/lib:/home/aralab/ros2_foxy/install/statistics_msgs/lib:/home/aralab/ros2_foxy/install/tracetools/lib:/home/aralab/ros2_foxy/install/sensor_msgs/lib:/home/aralab/ros2_foxy/install/geometry_msgs/lib:/home/aralab/ros2_foxy/install/std_msgs/lib:/home/aralab/ros2_foxy/install/builtin_interfaces/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_c/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_c/lib:/home/aralab/ros2_foxy/install/rcpputils/lib:/home/aralab/ros2_foxy/install/rosidl_runtime_c/lib:/home/aralab/ros2_foxy/install/rcutils/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libimage_transport_plugins.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/list_transports" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/list_transports")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/list_transports"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/image_transport" TYPE EXECUTABLE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/list_transports")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/list_transports" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/list_transports")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/list_transports"
         OLD_RPATH "/home/aralab/ASBIR-ROS2/build/image_transport:/home/aralab/ros2_foxy/install/message_filters/lib:/home/aralab/ros2_foxy/install/ament_index_cpp/lib:/home/aralab/ros2_foxy/install/class_loader/lib:/home/aralab/ros2_foxy/install/console_bridge_vendor/lib:/home/aralab/ros2_foxy/install/rclcpp/lib:/home/aralab/ros2_foxy/install/libstatistics_collector/lib:/home/aralab/ros2_foxy/install/rcl/lib:/home/aralab/ros2_foxy/install/rcl_interfaces/lib:/home/aralab/ros2_foxy/install/rmw_implementation/lib:/home/aralab/ros2_foxy/install/rmw/lib:/home/aralab/ros2_foxy/install/rcl_logging_spdlog/lib:/home/aralab/ros2_foxy/install/rcl_yaml_param_parser/lib:/home/aralab/ros2_foxy/install/libyaml_vendor/lib:/home/aralab/ros2_foxy/install/rosgraph_msgs/lib:/home/aralab/ros2_foxy/install/statistics_msgs/lib:/home/aralab/ros2_foxy/install/tracetools/lib:/home/aralab/ros2_foxy/install/sensor_msgs/lib:/home/aralab/ros2_foxy/install/geometry_msgs/lib:/home/aralab/ros2_foxy/install/std_msgs/lib:/home/aralab/ros2_foxy/install/builtin_interfaces/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_c/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_c/lib:/home/aralab/ros2_foxy/install/rcpputils/lib:/home/aralab/ros2_foxy/install/rosidl_runtime_c/lib:/home/aralab/ros2_foxy/install/rcutils/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/list_transports")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/republish" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/republish")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/republish"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/image_transport" TYPE EXECUTABLE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/republish")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/republish" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/republish")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/republish"
         OLD_RPATH "/home/aralab/ASBIR-ROS2/build/image_transport:/home/aralab/ros2_foxy/install/message_filters/lib:/home/aralab/ros2_foxy/install/ament_index_cpp/lib:/home/aralab/ros2_foxy/install/class_loader/lib:/home/aralab/ros2_foxy/install/console_bridge_vendor/lib:/home/aralab/ros2_foxy/install/rclcpp/lib:/home/aralab/ros2_foxy/install/libstatistics_collector/lib:/home/aralab/ros2_foxy/install/rcl/lib:/home/aralab/ros2_foxy/install/rcl_interfaces/lib:/home/aralab/ros2_foxy/install/rmw_implementation/lib:/home/aralab/ros2_foxy/install/rmw/lib:/home/aralab/ros2_foxy/install/rcl_logging_spdlog/lib:/home/aralab/ros2_foxy/install/rcl_yaml_param_parser/lib:/home/aralab/ros2_foxy/install/libyaml_vendor/lib:/home/aralab/ros2_foxy/install/rosgraph_msgs/lib:/home/aralab/ros2_foxy/install/statistics_msgs/lib:/home/aralab/ros2_foxy/install/tracetools/lib:/home/aralab/ros2_foxy/install/sensor_msgs/lib:/home/aralab/ros2_foxy/install/geometry_msgs/lib:/home/aralab/ros2_foxy/install/std_msgs/lib:/home/aralab/ros2_foxy/install/builtin_interfaces/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_introspection_c/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_cpp/lib:/home/aralab/ros2_foxy/install/rosidl_typesupport_c/lib:/home/aralab/ros2_foxy/install/rcpputils/lib:/home/aralab/ros2_foxy/install/rosidl_runtime_c/lib:/home/aralab/ros2_foxy/install/rcutils/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/image_transport/republish")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/aralab/ASBIR-ROS2/src/image_common/image_transport/include/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/environment" TYPE FILE FILES "/home/aralab/ros2_foxy/install/ament_package/lib/python3.8/site-packages/ament_package/template/environment_hook/library_path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/environment" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_environment_hooks/library_path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/image_transport")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/image_transport")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/environment" TYPE FILE FILES "/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/environment" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/environment" TYPE FILE FILES "/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/environment" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_environment_hooks/path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_environment_hooks/local_setup.bash")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_environment_hooks/local_setup.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_environment_hooks/package.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_index/share/ament_index/resource_index/packages/image_transport")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/image_transport__pluginlib__plugin" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_index/share/ament_index/resource_index/image_transport__pluginlib__plugin/image_transport")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/cmake" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_export_include_directories/ament_cmake_export_include_directories-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/cmake" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_export_libraries/ament_cmake_export_libraries-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/cmake" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_export_dependencies/ament_cmake_export_dependencies-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport/cmake" TYPE FILE FILES
    "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_core/image_transportConfig.cmake"
    "/home/aralab/ASBIR-ROS2/build/image_transport/ament_cmake_core/image_transportConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_transport" TYPE FILE FILES "/home/aralab/ASBIR-ROS2/src/image_common/image_transport/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/aralab/ASBIR-ROS2/build/image_transport/gtest/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/aralab/ASBIR-ROS2/build/image_transport/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")