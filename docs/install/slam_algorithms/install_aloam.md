# Install A-LOAM on Ubuntu

This guide provides step-by-step instructions to install A-LOAM from source on Ubuntu 20.04.

A-LOAM is an Advanced implementation of LOAM (J. Zhang and S. Singh. LOAM: Lidar Odometry and Mapping in Real-time), which uses Eigen and Ceres Solver to simplify code structure.

- **Official Documentation**: 
  - [LOAM GitHub Repository](https://github.com/laboshinl/loam_velodyne)
  - [A-LOAM GitHub Repository](https://github.com/HKUST-Aerial-Robotics/A-LOAM)
- **Operating System**: Ubuntu 20.04.6 LTS ([Download Link](https://releases.ubuntu.com/focal))
- **ROS Version**: ROS Noetic ([Documentation](https://wiki.ros.org/noetic))
- **Last Updated**: November 22, 2024

## Installation Steps

### Dependencies

Ensure the following libraries and packages are installed on your system:

- [**Eigen**](https://gitlab.com/libeigen/eigen): `sudo apt install libeigen3-dev`
- [**PCL**](https://github.com/PointCloudLibrary/pcl): `sudo apt install libpcl-dev`
- [**Ceres Solver**](http://ceres-solver.org): Follow the installation guide [here](/docs/install/dependencies/install_ceres_solver.md)

### Install A-LOAM

Follow these steps to install A-LOAM for ROS 1:

```sh
# ROS 1 environment setup
source /opt/ros/noetic/setup.bash

# Create workspace and move to src folder
mkdir -p ~/ros1_ws/src && cd ~/ros1_ws/src

# Clone the repository (frok from A-LOAM with compatibility for ROS Noetic)
git clone https://github.com/Thorfr123/A-LOAM

# Go back to the workspace root and build the package
cd .. && catkin_make

# Source the workspace setup file
source devel/setup.bash
```

## Additional Notes

The provided fork of A-LOAM addresses key compatibility issues with recent library versions and ROS Noetic.

### Library Compatibility

- **PCL**: Updated to use C++14 in `CMakeLists.txt` for compatibility with recent PCL versions:
  - **Old**: `-std=c++11`
  - **New**: `-std=c++14`

- **Ceres Solver**: Replaced deprecated `ceres::LocalParameterization` with `ceres::Manifold` in relevant files:
  - **Old**: `ceres::LocalParameterization *q_parameterization = new ceres::EigenQuaternionParameterization();`
  - **New**: `ceres::Manifold *q_parameterization = new ceres::EigenQuaternionManifold();`

### Frame ID Compatibility with ROS Noetic

To ensure RViz compatibility in ROS Noetic, which treats frame IDs as absolute by default, all frame IDs were updated to remove leading `/` characters:
  - **Old**: `/camera_init`
  - **New**: `camera_init`

Additional adjustments to frame IDs were made to standardize benchmarking across SLAM algorithms, though these are not essential for running A-LOAM in ROS Noetic.