# slam_benchmark_ros1_conf

**Version 0.1.0**

This repository implements the launch files required for the benchmark of 3D LiDAR-based SLAM algorithms implemented in ROS1. The package is based on 
the INESC TEC Robotics Navigation Stack that it allows you to have different configurations implemented and selecting just one based on your environment variables.

**Supported configurations in this version:**

- `aloam` configuration ([A-LOAM](https://github.com/HKUST-Aerial-Robotics/A-LOAM))
- `lego_loam_bor` configuration ([LeGO-LOAM-BOR](https://github.com/facontidavide/LeGO-LOAM-BOR))
- `liorf` configuration ([LIORF](https://github.com/YJZLuckyBoy/liorf))
- `dlio` configuration ([DLIO](https://github.com/vectr-ucla/direct_lidar_inertial_odometry))

**Supported 3D LiDAR sensors in this version:**

The following list of sensors is related to the [IILABS 3D dataset](https://rdm.inesctec.pt/dataset/nis-2025-001). For more informations please refer to the [iilabs3d-toolkit](https://github.com/JorgeDFR/iilabs3d-toolkit) GitHub page.

- `velodyne_vlp_16`
- `robosense_rs_helios_5515`
- `ouster_os1_64`
- `livox_mid_360`

>**Note**: Not all the algorithms support all the sensors, namely the A-LOAM, LeGO-LOAM-BOR and LIORF do not support the livox_mid_360 sensor.

## ROS

- [Ubuntu 20.04.5 LTS](https://releases.ubuntu.com/focal/)
- [ROS Noetic](https://wiki.ros.org/noetic)

## Usage

### Setup

```sh
# SLAM algorithm configuration
export SLAM_CONF=<configuration>  # (default: aloam)
# Dataset sensor
export SLAM_SENSOR=<sensor>       # (default: velodyne_vlp_16)
```

### Compilation

```sh
# ROS 1 environment setup
source source /opt/ros/noetic/setup.bash

# Create workspace
mkdir -p ~/ros1_ws/src

# Clone the repository
cd ~/ros1_ws/src
git clone https://gitlab.inesctec.pt/mrdt/projects/greenauto/benchmark-indoor-3d-localization

# Build
cd ~/ros1_ws
catkin_make
# OR catkin_make_isolated (more slow, build and check dependencies individually)
# OR catkin build (requires the Pyhton-based catkin tools)
source devel/setup.bash
```

### Launch

```sh
roslaunch slam_benchmark_conf slam_benchmark.launch
```

## Acknowledges

- [Faculty of Engineering, University of Porto (FEUP)](https://sigarra.up.pt/feup/en/)
- [INESC TEC - Institute for Systems and Computer Engineering, Technology and Science](https://www.inesctec.pt/en/)

## Contacts

If you have any questions or you want to know more about this work, please contact one of the contributors of this package:

- Jorge Diogo Ribeiro ([github](https://github.com/JorgeDFR),
  [gitlab](https://gitlab.inesctec.pt/jorge.d.ribeiro),
  [mail:inesctec](mailto:jorge.d.ribeiro@inesctec.pt))
- Ricardo B. Sousa ([github](https://github.com/sousarbarb/),
  [gitlab](https://gitlab.inesctec.pt/ricardo.b.sousa),
  [mail:inesctec](mailto:ricardo.b.sousa@inesctec.pt))
- Héber Miguel Sobreira ([github](https://github.com/HeberSobreira),
  [gitlab](https://gitlab.inesctec.pt/heber.m.sobreira),
  [mail:inesctec](mailto:heber.m.sobreira@inesctec.pt))