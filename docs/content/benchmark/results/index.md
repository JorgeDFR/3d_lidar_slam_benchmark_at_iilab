# Benchmark Results

In this section, we present an evaluation of the selected LiDAR-based SLAM algorithms' performance on the [IILABS 3D dataset](../../dataset/index.md). 
All result pages include detailed tables with performance metrics as well as trajectory plots for each experimental sequence.

Each result page offers both quantitative and qualitative results for different SLAM algorithm, 3D LiDAR sensor, and dataset sequence combinations:

- **Performance Tables:** Comparative accuracy metrics (ATE, RTE, RRE);
- **Trajectory Plots:** Visual representations of the odometry trajectories.

---

## Approaches to Explore the Results

There are two complementary perspectives for analysing the results:

### :material-robot: Results by SLAM Algorithm

This view groups results by individual SLAM algorithms. 
Each page details the performance obtained when using all sensor combinations with the selected algorithm. 
Use this perspective to assess the impact of sensor inputs on a single SLAM method.

- [A-LOAM](slam_algorithms/aloam.md)
- [LeGO-LOAM-BOR](slam_algorithms/lego_loam_bor.md)
- [LIORF](slam_algorithms/liorf.md)
- [DLIO](slam_algorithms/dlio.md)
- [VineSLAM](slam_algorithms/vineslam.md)
- [KISS-ICP](slam_algorithms/kiss_icp.md)
- [GLIM](slam_algorithms/glim.md)
- [Kinematic-ICP](slam_algorithms/kinematic_icp.md)
- [MOLA-LO](slam_algorithms/mola_lo.md)

---

### :material-rotate-3d: Results by 3D LiDAR Sensor

This perspective organizes results by the specific 3D LiDAR sensor used in the experiments. 
Each page presents the performance metrics and trajectory plots for all SLAM algorithms when using that particular sensor. 
This approach highlights the influence of sensor characteristics, such as scanning pattern, resolution, and field-of-view, on overall SLAM performance.

- [Livox Mid-360](3d_lidar_sensors/livox_mid-360.md)
- [Ouster OS1-64](3d_lidar_sensors/ouster_os1-64.md)
- [RoboSense RS-Helios-5515](3d_lidar_sensors/robosense_rs-helios-5515.md)
- [Velodyne VLP-16](3d_lidar_sensors/velodyne_vlp-16.md)

---

Choose the perspective that best meets your exploration needs. Whether you're interested in the performance of a specific algorithm across all sensors or in understanding how a particular sensor affects SLAM performance across multiple algorithms, our benchmark results are designed to offer a clear and comprehensive analysis.