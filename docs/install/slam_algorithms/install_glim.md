# Install GLIM on Ubuntu

This guide provides step-by-step instructions to install GLIM from source on Ubuntu 22.04.

- **Official Documentation**: [GLIM Installation](https://koide3.github.io/glim/installation.html)
- **Tested OS**: [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy)
- **ROS Version**: [ROS Humble](https://wiki.ros.org/noetic)
- **Last Updated**: November 22, 2024

## Installation Steps

### Dependencies

Run the following command to install the required dependencies:

```sh
sudo apt install libomp-dev libboost-all-dev libmetis-dev \
                 libfmt-dev libspdlog-dev libopencv-dev \
                 libglm-dev libglfw3-dev libpng-dev libjpeg-dev
```

Additionally, ensure you have the following components:

- [**GTSAM**](https://github.com/borglab/gtsam): Follow the installation guide [here](/docs/install/dependencies/install_gtsam_42a9.md)
- [**gtsam_points**](https://github.com/koide3/gtsam_points): Follow the installation guide [here](/docs/install/dependencies/install_gtsam_points.md)
- [**Iridescence**](https://github.com/koide3/iridescence): Follow the installation guide [here](/docs/install/dependencies/install_iridescence.md) (Optional - visualization alternative to RViz)
- [**CUDA**](https://developer.nvidia.com/cuda-toolkit): Follow the installation guide [here](https://developer.nvidia.com/cuda-toolkit) (Optional - for GPU parallel processing)

### Install GLIM ROS 1

Follow these steps to install GLIM for ROS 1:

```sh
# Make shared libraries visible to the system
sudo ldconfig

# ROS 1 environment setup
source /opt/ros/noetic/setup.bash

# Create workspace and move to src folder
mkdir -p ~/ros1_ws/src && cd ~/ros1_ws/src

# Clone the repositories
git clone https://github.com/koide3/glim
git clone https://github.com/koide3/glim_ros1

# Notes:
# - GLIM uses DBUILD_WITH_CUDA=ON and DBUILD_WITH_VIEWER=ON by default.
#   Change the flags in the CMakeLists.txt of both glim and glim_ros1 if you do not want to use CUDA and/or Iridescence.
# - Additionally, if you set the flag DBUILD_WITH_VIEWER=OFF in glim_ros1, you need to remove or comment out the 'offline_viewer' in the install call.

# Go back to the workspace root
cd .. && catkin_make

# Source the workspace setup file
source devel/setup.bash
```

## Additional Notes
- GLIM also provides a wrapper for ROS 1 (Noetic). For more details, please refer to the official documentation.