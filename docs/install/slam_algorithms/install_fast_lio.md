# Install Fast-LIO on Ubuntu

This guide provides step-by-step instructions to install Fast-LIO from source on Ubuntu 20.04.

- **Official Documentation**: [Fast-LIO Github Repository](https://github.com/hku-mars/FAST_LIO)
- **Tested OS**: [Ubuntu 20.04.6 LTS](https://releases.ubuntu.com/focal)
- **ROS Version**: [ROS Noetic](https://wiki.ros.org/noetic)
- **Last Updated**: November 22, 2024

## Installation Steps

### Dependencies

Ensure you have the following components:

- [**Eigen**](https://gitlab.com/libeigen/eigen): `sudo apt install libeigen3-dev`
- [**PCL**](https://github.com/PointCloudLibrary/pcl): `sudo apt install libpcl-dev`
- [**Livox-SDK**](/docs/install/dependencies/install_livox_sdk.md)
- [**livox_ros_driver**](https://github.com/Livox-SDK/livox_ros_driver)

### Install Fast-LIO

Follow these steps to install Fast-LIO for ROS 1:

```sh
# ROS 1 environment setup
source /opt/ros/noetic/setup.bash

# Create workspace and move to src folder
mkdir -p ~/ros1_ws/src && cd ~/ros1_ws/src

# Clone the repository (frok from Fast-LIO with compilation bug fix)
git clone https://github.com/Thorfr123/FAST_LIO --recursive

# Go back to the workspace root and build the package
cd .. && catkin_make

# Source the workspace setup file
source devel/setup.bash
```

## Additional Notes
- Fast-LIO also provides a wrapper for ROS 2 (Foxy / Galatic). For more details, please refer to the official documentation.