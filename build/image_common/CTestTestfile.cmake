# CMake generated Testfile for 
# Source directory: /home/aralab/ASBIR-ROS2/src/image_common/image_common
# Build directory: /home/aralab/ASBIR-ROS2/build/image_common
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(copyright "/usr/bin/python3" "-u" "/home/aralab/ros2_foxy/install/ament_cmake_test/share/ament_cmake_test/cmake/run_test.py" "/home/aralab/ASBIR-ROS2/build/image_common/test_results/image_common/copyright.xunit.xml" "--package-name" "image_common" "--output-file" "/home/aralab/ASBIR-ROS2/build/image_common/ament_copyright/copyright.txt" "--command" "/home/aralab/ros2_foxy/install/ament_copyright/bin/ament_copyright" "--xunit-file" "/home/aralab/ASBIR-ROS2/build/image_common/test_results/image_common/copyright.xunit.xml")
set_tests_properties(copyright PROPERTIES  LABELS "copyright;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/aralab/ASBIR-ROS2/src/image_common/image_common" _BACKTRACE_TRIPLES "/home/aralab/ros2_foxy/install/ament_cmake_test/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/aralab/ros2_foxy/install/ament_cmake_copyright/share/ament_cmake_copyright/cmake/ament_copyright.cmake;41;ament_add_test;/home/aralab/ros2_foxy/install/ament_cmake_copyright/share/ament_cmake_copyright/cmake/ament_cmake_copyright_lint_hook.cmake;18;ament_copyright;/home/aralab/ros2_foxy/install/ament_cmake_copyright/share/ament_cmake_copyright/cmake/ament_cmake_copyright_lint_hook.cmake;0;;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/aralab/ros2_foxy/install/ament_lint_auto/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;21;ament_execute_extensions;/home/aralab/ros2_foxy/install/ament_lint_auto/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;0;;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_package.cmake;66;ament_execute_extensions;/home/aralab/ASBIR-ROS2/src/image_common/image_common/CMakeLists.txt;10;ament_package;/home/aralab/ASBIR-ROS2/src/image_common/image_common/CMakeLists.txt;0;")
add_test(lint_cmake "/usr/bin/python3" "-u" "/home/aralab/ros2_foxy/install/ament_cmake_test/share/ament_cmake_test/cmake/run_test.py" "/home/aralab/ASBIR-ROS2/build/image_common/test_results/image_common/lint_cmake.xunit.xml" "--package-name" "image_common" "--output-file" "/home/aralab/ASBIR-ROS2/build/image_common/ament_lint_cmake/lint_cmake.txt" "--command" "/home/aralab/ros2_foxy/install/ament_lint_cmake/bin/ament_lint_cmake" "--xunit-file" "/home/aralab/ASBIR-ROS2/build/image_common/test_results/image_common/lint_cmake.xunit.xml")
set_tests_properties(lint_cmake PROPERTIES  LABELS "lint_cmake;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/aralab/ASBIR-ROS2/src/image_common/image_common" _BACKTRACE_TRIPLES "/home/aralab/ros2_foxy/install/ament_cmake_test/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/aralab/ros2_foxy/install/ament_cmake_lint_cmake/share/ament_cmake_lint_cmake/cmake/ament_lint_cmake.cmake;41;ament_add_test;/home/aralab/ros2_foxy/install/ament_cmake_lint_cmake/share/ament_cmake_lint_cmake/cmake/ament_cmake_lint_cmake_lint_hook.cmake;21;ament_lint_cmake;/home/aralab/ros2_foxy/install/ament_cmake_lint_cmake/share/ament_cmake_lint_cmake/cmake/ament_cmake_lint_cmake_lint_hook.cmake;0;;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/aralab/ros2_foxy/install/ament_lint_auto/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;21;ament_execute_extensions;/home/aralab/ros2_foxy/install/ament_lint_auto/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;0;;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_package.cmake;66;ament_execute_extensions;/home/aralab/ASBIR-ROS2/src/image_common/image_common/CMakeLists.txt;10;ament_package;/home/aralab/ASBIR-ROS2/src/image_common/image_common/CMakeLists.txt;0;")
add_test(xmllint "/usr/bin/python3" "-u" "/home/aralab/ros2_foxy/install/ament_cmake_test/share/ament_cmake_test/cmake/run_test.py" "/home/aralab/ASBIR-ROS2/build/image_common/test_results/image_common/xmllint.xunit.xml" "--package-name" "image_common" "--output-file" "/home/aralab/ASBIR-ROS2/build/image_common/ament_xmllint/xmllint.txt" "--command" "/home/aralab/ros2_foxy/install/ament_xmllint/bin/ament_xmllint" "--xunit-file" "/home/aralab/ASBIR-ROS2/build/image_common/test_results/image_common/xmllint.xunit.xml")
set_tests_properties(xmllint PROPERTIES  LABELS "xmllint;linter" TIMEOUT "60" WORKING_DIRECTORY "/home/aralab/ASBIR-ROS2/src/image_common/image_common" _BACKTRACE_TRIPLES "/home/aralab/ros2_foxy/install/ament_cmake_test/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/aralab/ros2_foxy/install/ament_cmake_xmllint/share/ament_cmake_xmllint/cmake/ament_xmllint.cmake;50;ament_add_test;/home/aralab/ros2_foxy/install/ament_cmake_xmllint/share/ament_cmake_xmllint/cmake/ament_cmake_xmllint_lint_hook.cmake;18;ament_xmllint;/home/aralab/ros2_foxy/install/ament_cmake_xmllint/share/ament_cmake_xmllint/cmake/ament_cmake_xmllint_lint_hook.cmake;0;;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/aralab/ros2_foxy/install/ament_lint_auto/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;21;ament_execute_extensions;/home/aralab/ros2_foxy/install/ament_lint_auto/share/ament_lint_auto/cmake/ament_lint_auto_package_hook.cmake;0;;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_execute_extensions.cmake;48;include;/home/aralab/ros2_foxy/install/ament_cmake_core/share/ament_cmake_core/cmake/core/ament_package.cmake;66;ament_execute_extensions;/home/aralab/ASBIR-ROS2/src/image_common/image_common/CMakeLists.txt;10;ament_package;/home/aralab/ASBIR-ROS2/src/image_common/image_common/CMakeLists.txt;0;")