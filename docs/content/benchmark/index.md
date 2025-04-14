# Benchmark

This section presents the methodology, experimental protocols, and comparative results for the SLAM algorithms evaluated on our [IILABS 3D dataset](https://rdm.inesctec.pt/dataset/nis-2025-001). By combining state-of-the-art SLAM algorithms with rich sensor data, our benchmark provides insights on performance in the following accuracy metrics:

- Absolute Trajectory Error (ATE)
- Relative Translational Error (RTE)
- Relative Rotational Error (RRE)

Our goal is to support researchers in understanding the trade-offs and strengths of different approaches in challenging indoor environments.

---

## :material-robot: [SLAM Algorithms](slam_algorithms.md)

The SLAM algorithms page features a detailed comparison of the state-of-the-art SLAM methods considered in the benchmark analysis. 
For each algorithm, you’ll find:

- SLAM algorithm paper link;
- Open-source code repository link;
- Supported ROS version;
- Compatibility with the different 3D LiDARs configurations;
- Key features, such as IMU and/or wheel odometry sensor fusion support, and loop closure detection;
- The publication year for reference.

---

## :material-chart-line: [Results](results/index.md)

The Results section presents both quantitative and qualitative assessments. Here you will find:

- **ATE, RTE, and RRE metrics:** Comparative tables showing performance across different sensor setups and experimental sequences.
- **Trajectory Plots:** Visualizations of the odometry trajectories for each sensor and algorithm.

These detailed comparisons help identify the strengths and limitations of each SLAM approach under varied conditions.

---

## :material-docker: [Docker Environment](docker.md)

For reproducibility and ease of experimentation, our benchmark incorporates a Dockerized environment. 
This section covers:

- The containerized setup and dependencies;
- Scripts and instructions to run the benchmark experiments;
- Tips for replicating the results on your own system.

---

## Overview & Navigation

Our benchmark is organized to streamline your review:

- Begin with *SLAM Algorithms* to understand the methods and their individual attributes;
- Move to *Results* to explore the performance metrics and trajectory visualizations;
- Finally, review the *Docker Environment* to replicate or extend the experiments in your own setup.

By navigating through these sections, you will gain an in-depth perspective on the performance of LiDAR-based SLAM in an indoor setting.