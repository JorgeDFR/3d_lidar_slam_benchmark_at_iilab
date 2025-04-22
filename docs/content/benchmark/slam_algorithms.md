# SLAM Algorithms

The benchmark evaluates nine state-of-the-art 3D LiDAR-based SLAM algorithms:

1. **A-LOAM**: An advanced implementation of LOAM (LiDAR Odometry and Mapping)
2. **LeGO-LOAM-BOR**: A fork of LeGO-LOAM with good software engineering practices to make the code more readable and efficient
3. **LIORF**: A fork of LIO-SAM which removes the feature extraction module and makes it easier to adapt other sensors
4. **DLIO**: A lightweight LiDAR-Inertial Odometry (LIO) algorithm with a coarse-to-fine approach in constructing continuous-time trajectories for precise motion correction
5. **VineSLAM**: A localization and mapping algorithm designed for challenging agricultural environments
6. **KISS-ICP**: An LiDAR Odometry ICP pipeline with the KISS principle (Keep It Simple and Scalable)
7. **GLIM**: An versatile and extensible range-based 3D mapping framework
8. **Kinematic-ICP**: An LiDAR Odometry ICP pipeline with kinematic constraints for wheeled robots
9. **MOLA-LO**: A modular optimization framework for localization and mapping using LiDAR Odometry (LO)

| SLAM Algorithm                                                                 | Code Repository                                                          | ROS Version    | VLP-16 | OS1-64 | RS-5515 | Mid-360 | IMU | Wheel Odom | Loop Closure  | Year |
| :----------------------------------------------------------------------------- | :----------------------------------------------------------------------- | :------------: | :----: | :----: | :-----: | :-----: | :-: | :--------: | :-: | :--: |
| [**LOAM**](https://ri.cmu.edu/pub_files/2014/7/Ji_LidarMapping_RSS2014_v8.pdf) | [A-LOAM](https://github.com/HKUST-Aerial-Robotics/A-LOAM)                | Noetic (ROS 1) | X      | X      | X       | -       | -   | -          | -   | 2014 |
| [**LeGO-LOAM**](https://doi.org/10.1109/IROS.2018.8594299)                     | [LeGO-LOAM-BOR](https://github.com/facontidavide/LeGO-LOAM-BOR)          | Noetic (ROS 1) | X      | X      | X       | -       | -   | -          | X   | 2018 |
| [**LIO-SAM**](https://doi.org/10.1109/IROS45743.2020.9341176)                  | [LIORF](https://github.com/YJZLuckyBoy/liorf)                            | Noetic (ROS 1) | X      | X      | X       | -       | X   | -          | X   | 2020 |
| [**DLIO**](https://doi.org/10.1109/ICRA48891.2023.10160508)                    | [Official](https://github.com/vectr-ucla/direct_lidar_inertial_odometry) | Noetic (ROS 1) | X      | X      | X       | X       | X   | -          | -   | 2022 |
| [**VineSLAM**](https://doi.org/10.3389/frobt.2022.832165)                      | [Official](https://gitlab.inesctec.pt/agrob/prototypes/vineslam-os)      | Humble (ROS 2) | X      | X      | X       | X       | X   | X          | -   | 2022 |
| [**KISS-ICP**](https://doi.org/10.1109/LRA.2023.3236571)                       | [Official](https://github.com/PRBonn/kiss-icp)                           | Humble (ROS 2) | X      | X      | X       | X       | -   | -          | -   | 2023 |
| [**GLIM**](https://doi.org/10.1016/j.robot.2024.104750)                        | [Official](https://github.com/koide3/glim)                               | Humble (ROS 2) | X      | X      | X       | X       | X   | -          | X   | 2024 |
| [**Kinematic-ICP**](https://arxiv.org/pdf/2410.10277)                          | [Official](https://github.com/PRBonn/kinematic-icp)                      | Humble (ROS 2) | X      | X      | X       | X       | -   | X          | -   | 2024 |
| [**MOLA-LO**](https://doi.org/10.1177/02783649251316881)                       | [Official](https://github.com/MOLAorg/mola_lidar_odometry)               | Humble (ROS 2) | X      | X      | X       | X       | -   | -          | -   | 2024 |