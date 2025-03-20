# VineSLAM

## Absolute Trajectory Error (ATE)

Root Mean Square Error (RMSE) of the absolute position differences. Values are presented in meters (m).

| 3D LiDAR Sensor              | Nav A Diff     | Nav A Omni     | Loop           | Slippage       | Ramp           |
| :--------------------------- | :------------: | :------------: | :------------: | :------------: | :------------: |
| **Velodyne VLP-16**          | 0.083 m | 0.089 m | 0.128 m | 0.077 m | 0.048 m |
| **Ouster OS1-64**            | 0.144 m | 0.139 m | 0.143 m | 0.147 m | 0.086 m |
| **RoboSense RS-Helios-5515** | 0.108 m | 0.078 m | 0.123 m | 0.095 m | 0.056 m |
| **Livox Mid 360**            | 0.188 m | 0.106 m | 0.124 m | 0.096 m | 0.108 m |

## Relative Translational Error (RTE)

Mean value calculated over all 10-meter segments. Values are presented as a percentage (%).

| 3D LiDAR Sensor              | Nav A Diff   | Nav A Omni   | Loop         | Slippage     | Ramp         |
| :--------------------------- | :----------: | :----------: | :----------: | :----------: | :----------: |
| **Velodyne VLP-16**          | 2.03% | 2.00% | 2.24% | 2.18% | 0.62% |
| **Ouster OS1-64**            | 2.61% | 2.86% | 2.83% | 2.57% | 1.08% |
| **RoboSense RS-Helios-5515** | 2.00% | 1.97% | 2.55% | 1.67% | 0.80% |
| **Livox Mid 360**            | 2.70% | 1.95% | 2.07% | 1.56% | 1.12% |

## Relative Rotational Error (RRE)

Mean value calculated over all 10-meter segments. Values are presented in degrees per meter (°/m).

| 3D LiDAR Sensor              | Nav A Diff       | Nav A Omni       | Loop             | Slippage         | Ramp             |
| :--------------------------- | :--------------: | :--------------: | :--------------: | :--------------: | :--------------: |
| **Velodyne VLP-16**          | 0.147 °/m | 0.166 °/m | 0.182 °/m | 0.148 °/m | 0.283 °/m |
| **Ouster OS1-64**            | 0.201 °/m | 0.242 °/m | 0.251 °/m | 0.153 °/m | 0.369 °/m |
| **RoboSense RS-Helios-5515** | 0.148 °/m | 0.177 °/m | 0.199 °/m | 0.111 °/m | 0.315 °/m |
| **Livox Mid 360**            | 0.223 °/m | 0.188 °/m | 0.146 °/m | 0.072 °/m | 0.335 °/m |

## Trajectory Plots
