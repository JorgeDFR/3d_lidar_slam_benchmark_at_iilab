cmake_minimum_required(VERSION 3.5)
project(slam_benchmark_ros1_conf)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find catkin macros and libraries
find_package(catkin REQUIRED)

# Catkin specific configuration
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES slam_benchmark_conf
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

# Installation rules
install(
  DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)