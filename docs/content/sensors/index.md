# Sensors

This section provides detailed information about all the sensors used in the [IILABS 3D dataset](https://rdm.inesctec.pt/dataset/nis-2025-001), including 3D LiDARs, 2D laser scanners, and inertial measurement units (IMUs).

For each sensor, we provide:

- :material-file-document-outline: Technical specifications  
- :material-database-outline: Usage details within the dataset  
- :material-link-variant: Manufacturer documentation  
- :material-cube-outline: 3D models (where available)

We organize the sensors into three main categories:

---

## :material-cube-scan: [3D LiDARs](lidar3d/index.md)

3D LiDAR sensors form the core of this benchmark. The dataset includes sequences from four different sensors, featuring both mechanical spinning and non-repetitive scanning designs.

---

## :material-line-scan: [2D Laser Scanners](lidar2d/index.md)

The dataset includes data from a Hokuyo UST-10LX, a time-of-flight 2D laser scanner. It was used alongside a 2D navigation stack to ensure consistent trajectory patterns across all 3D LiDAR recordings.

---

## :material-rotate-orbit: [Inertial Measurement Units (IMUs)](imu/index.md)

IMUs enable accurate motion tracking and orientation estimation, making them a valuable complementary sensor in SLAM applications. In our dataset we include data from the Xsens MTi-630 AHRS to benchmark SLAM performance with and without IMU sensor fusion.

---