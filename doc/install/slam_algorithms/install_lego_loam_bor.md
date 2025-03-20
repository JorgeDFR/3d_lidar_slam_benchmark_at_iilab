# Install LeGO-LOAM-BOR on Ubuntu

This guide provides step-by-step instructions to install LeGO-LOAM-BOR from source on Ubuntu 20.04.

LeGO-LOAM-BOR is a fork from the original LeGO-LOAM, that enhances code readability, performance, and efficiency while preserving the original algorithm.

- **Official Documentation**: 
  - [LeGO-LOAM GitHub Repository](https://github.com/RobustFieldAutonomyLab/LeGO-LOAM)
  - [LeGO-LOAM-BOR Github Repository](https://github.com/facontidavide/LeGO-LOAM-BOR)
- **Tested OS**: [Ubuntu 20.04.6 LTS](https://releases.ubuntu.com/focal)
- **ROS Version**: [ROS Noetic](https://wiki.ros.org/noetic)
- **Last Updated**: November 22, 2024

## Installation Steps

### Dependencies

Ensure you have the following components:

- [**Eigen**](https://gitlab.com/libeigen/eigen): `sudo apt install libeigen3-dev`
- [**PCL**](https://github.com/PointCloudLibrary/pcl): `sudo apt install libpcl-dev`
- [**TBB**](https://github.com/oneapi-src/oneTBB): `sudo apt install libtbb-dev`
- [**GTSAM**](https://github.com/borglab/gtsam): Follow the installation guide [here](/doc/install/dependencies/install_gtsam_403.md)

### Install LeGO-LOAM-BOR

Follow these steps to install LeGO-LOAM for ROS 1:

```sh
# ROS 1 environment setup
source /opt/ros/noetic/setup.bash

# Create workspace and move to src folder
mkdir -p ~/ros1_ws/src && cd ~/ros1_ws/src

# Clone the repository (frok from LeGO-LOAM-BOR with compatibility for ROS Noetic)
git clone https://github.com/Thorfr123/LeGO-LOAM-BOR

# Go back to the workspace root and build the package
cd .. && catkin_make

# Source the workspace setup file
source devel/setup.bash
```

## Additional Notes

The provided fork of LeGo-LOAM-BOR addresses key compatibility issues with recent library versions and ROS Noetic.

### Library Compatibility

- **PCL**: Updated to use C++14 in `CMakeLists.txt` for compatibility with recent PCL versions:
  - **Old**: `-std=c++11`
  - **New**: `-std=c++14`

### Frame ID Compatibility with ROS Noetic

To ensure RViz compatibility in ROS Noetic, which treats frame IDs as absolute by default, all frame IDs were updated to remove leading `/` characters:
  - **Old**: `/camera_init`
  - **New**: `camera_init`

Additional adjustments to frame IDs were made to standardize benchmarking across SLAM algorithms, though these are not essential for running LeGo-LOAM-BOR in ROS Noetic.