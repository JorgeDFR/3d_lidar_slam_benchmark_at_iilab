# IMU-LiDAR and IMU Intrinsic Calibration

This document provides resources and instructions for IMU-LiDAR extrinsic calibration and IMU intrinsic calibration.

---

## IMU Intrinsic Calibration

Intrinsic calibration of an IMU involves estimating its noise characteristics (e.g., white noise and bias instability) to improve the accuracy of sensor fusion and state estimation algorithms. The following resources and usage notes will guide you through the process.

### Tools
- **[Allan Variance ROS](https://github.com/ori-drs/allan_variance_ros)**: A ROS package for IMU intrinsic calibration using Allan variance analysis.

> **Notes**: Allan Variance calibration requires a **long rosbag** (~3 hours) with the IMU in a stationary position to collect sufficient data for analysis. Additionally, after processing the data, the calculated **white noise** and **bias instability** values should be **inflated** to account for real-world uncertainties and improve the robustness of sensor fusion algorithms (Recommended values **White Noise x5** and **Bias Instability x10**).

---

## IMU-LiDAR Extrinsic Calibration

Extrinsic calibration determines the precise spatial relationship between an IMU and a LiDAR sensor. The following tools provide robust methods for achieving this.

### Tools
- **[GRIL-Calib](https://github.com/Taeyoung96/GRIL-Calib)**: A ROS package for ground robot IMU-LiDAR extrinsic calibration.
- **[Awesome-LiDAR-IMU Calibration](https://github.com/Taeyoung96/Awesome-LiDAR-IMU-calibration)**: A curated list of alternative IMU-LiDAR calibration tools.

> **Notes**: GRIL-Calib supports only spinning LiDARs (e.g., Velodyne, Ouster) and does not support solid-state LiDARs (e.g., Livox). Additionally, the recommended trajectory for the robots is and infinite loop (8 format).