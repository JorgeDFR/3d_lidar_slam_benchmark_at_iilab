# Install LIORF on Ubuntu

This guide provides step-by-step instructions to install LIORF from source on Ubuntu 20.04.

LIORF is a fork of the original LIO-SAM that adapts the main algorithm to support a wider variety of sensors, including 6-axis IMUs, low-frequency IMUs (e.g., 50 Hz, 100 Hz), and Robosense LiDAR sensors. Additionally, to simplify adaptation to different LiDAR sensors, such as Robosense, the feature extraction module was removed. Furthermore, the loop closure detection mechanism was replaced with a ScanContext-based approach.

- **Official Documentation**: 
  - [LIO-SAM GitHub Repository](https://github.com/TixiaoShan/LIO-SAM)
  - [LIORF Github Repository](https://github.com/YJZLuckyBoy/liorf)
- **Tested OS**: [Ubuntu 20.04.6 LTS](https://releases.ubuntu.com/focal)
- **ROS Version**: [ROS Noetic](https://wiki.ros.org/noetic)
- **Last Updated**: November 22, 2024

## Installation Steps

### Dependencies

Ensure you have the following components:

- [**Eigen**](https://gitlab.com/libeigen/eigen): `sudo apt install libeigen3-dev`
- [**PCL**](https://github.com/PointCloudLibrary/pcl): `sudo apt install libpcl-dev`
- [**OpenCV**](https://github.com/opencv/opencv): `sudo apt install libopencv-dev`
- [**GeographicLib**](https://github.com/geographiclib/geographiclib): `sudo apt install libgeographic-dev`
- [**GTSAM**](https://github.com/borglab/gtsam): Follow the installation guide [here](/doc/install/dependencies/install_gtsam_403.md)

### Install LIORF

Follow these steps to install LIORF for ROS 1:

```sh
# ROS 1 environment setup
source /opt/ros/noetic/setup.bash

# Create workspace and move to src folder
mkdir -p ~/slam_catkin_ws/src && cd ~/slam_catkin_ws/src

# Clone the repository (frok from liorf with robosense compatibility bug fix)
git clone https://github.com/Thorfr123/liorf

# Go back to the workspace root and build the package
cd .. && catkin_make

# Source the workspace setup file
source devel/setup.bash
```

## Additional Notes
- LIORF also provides a wrapper for ROS 2. For more details, please refer to the official documentation.