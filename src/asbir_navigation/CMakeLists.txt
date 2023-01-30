cmake_minimum_required(VERSION 3.5)
project(asbir_navigation)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(tf2_ros REQUIRED)

include_directories(include)

# CPP executables
add_executable(listener src/subscriber_member_function.cpp)
ament_target_dependencies(listener rclcpp std_msgs)
# add_executable(transform_point src/transform_point.cpp)
# ament_target_dependencies(transform_point rclcpp std_msgs geometry_msgs visualization_msgs tf2_ros)

install(TARGETS
  listener
  # transform_point
  DESTINATION lib/${PROJECT_NAME})

ament_python_install_package(${PROJECT_NAME})

# Python executables
install(PROGRAMS
  scripts/publisher_member_function.py
  scripts/modelTest.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()