# slam_benchmark_ros2_conf

**Version 0.1.0**

This repository implements the launch files required for the benchmark of 3D LiDAR-based SLAM algorithms implemented in ROS1. The package is based on 
the INESC TEC Robotics Navigation Stack that it allows you to have different configurations implemented and selecting just one based on your environment variables.

**Supported configurations in this version:**

- `vineslam` configuration ([VineSLAM](https://gitlab.inesctec.pt/agrob/prototypes/vineslam))
- `kiss_icp` configuration ([KISS-ICP](https://github.com/PRBonn/kiss-icp))
- `glim` configuration ([GLIM](https://github.com/koide3/glim))
- `kinematic_icp` configuration ([Kinematic-ICP](https://github.com/PRBonn/kinematic-icp))
- `mola_lo` configuration ([MOLA-LO](https://docs.mola-slam.org/latest/index.html))

**Supported 3D LiDAR sensors in this version:**

The following list of sensors is related to the [IILABS 3D dataset](https://rdm.inesctec.pt/dataset/nis-2025-001). For more informations please refer to the [iilabs3d-toolkit](https://github.com/JorgeDFR/iilabs3d-toolkit) GitHub page.

- `velodyne_vlp_16`
- `robosense_rs_helios_5515`
- `ouster_os1_64`
- `livox_mid_360`

## ROS

- [Ubuntu 22.04.5 LTS](https://releases.ubuntu.com/jammy/)
- [ROS Humble](https://docs.ros.org/en/humble/index.html)

## Usage

### Setup

```sh
# SLAM algorithm configuration
export SLAM_CONF=<configuration>  # (default: kiss_icp)
# Dataset sensor
export SLAM_SENSOR=<sensor>       # (default: velodyne_vlp_16)
```

### Compilation

```sh
# ROS 2 environment setup
source source /opt/ros/humble/setup.bash

# Create workspace
mkdir -p ~/ros2_ws/src

# Clone the repository
cd ~/ros2_ws/src
git clone https://gitlab.inesctec.pt/mrdt/projects/greenauto/benchmark-indoor-3d-localization

# Build
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Launch

```sh
ros2 launch slam_benchmark_ros2_conf slam_benchmark.launch.xml
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