# Install KISS-ICP on Ubuntu

This guide provides step-by-step instructions to install KISS-ICP from source on Ubuntu 22.04.

- **Official Documentation**: [KISS-ICP Github Repository](https://github.com/PRBonn/kiss-icp)
- **Tested OS**: [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy)
- **ROS Version**: [ROS 2 Humble](https://docs.ros.org/en/humble/index.html)
- **Last Updated**: November 22, 2024

## Installation Steps

### Dependencies

Ensure you have the following components installed:

- [**Eigen**](https://gitlab.com/libeigen/eigen): `sudo apt install libeigen3-dev`
- [**Sophus**](https://github.com/strasdat/Sophus): `sudo apt install libsophus-dev`
- [**TBB**](https://github.com/oneapi-src/oneTBB): `sudo apt install libtbb-dev`
- [**Robin-map**](https://github.com/Tessil/robin-map): `sudo apt install robin-map-dev`

### Install Kiss-ICP

Follow these steps to install KISS-ICP for ROS 2:

```sh
# ROS 2 environment setup
source /opt/ros/humble/setup.bash

# Create workspace and move to src folder
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src

# Clone the repository
git clone https://github.com/PRBonn/kiss-icp

# Ensure all dependencies are installed
rosdep install --from-paths src --ignore-src -r -y

# Go back to the workspace root and build the package
cd .. && colcon build

# Source the workspace setup file
source install/setup.bash
```

## Additional Notes
- KISS-ICP also provides a wrapper for ROS 1, however it was deprecated in version 0.3.0. For more details, please refer to the official documentation.