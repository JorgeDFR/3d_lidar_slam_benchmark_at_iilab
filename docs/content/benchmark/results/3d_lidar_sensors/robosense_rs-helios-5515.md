# RoboSense RS-Helios-5515

## Absolute Trajectory Error (ATE)

Root Mean Square Error (RMSE) of the absolute position differences. Values are presented in meters (m).

| 3D LiDAR Sensor              | Nav A Diff     | Nav A Omni     | Loop           | Slippage       | Ramp           |
| :--------------------------- | :------------: | :------------: | :------------: | :------------: | :------------: |
| **A-LOAM**                   | 0.032 m | 0.032 m | 0.045 m | 0.042 m | 0.057 m |
| **LeGO-LOAM-BOR**            | 0.040 m | 0.038 m | 0.039 m | 0.043 m | 0.041 m |
| **LIORF**                    |  |  |  |  |  |
| **DLIO**                     |  |  |  |  |  |
| **VineSLAM**                 |  |  |  |  |  |
| **KISS-ICP**                 |  |  |  |  |  |
| **GLIM**                     |  |  |  |  |  |
| **Kinematic-ICP**            |  |  |  |  |  |
| **MOLA-LO**                  |  |  |  |  |  |

## Relative Translational Error (RTE)

Mean value calculated over all 10-meter segments. Values are presented as a percentage (%).

| 3D LiDAR Sensor              | Nav A Diff   | Nav A Omni   | Loop         | Slippage     | Ramp         |
| :--------------------------- | :----------: | :----------: | :----------: | :----------: | :----------: |
| **A-LOAM**                   | 0.92% | 1.05% | 1.03% | 1.32% | 0.59% |
| **LeGO-LOAM-BOR**            | 1.45% | 1.29% | 1.37% | 1.71% | 0.59% |
| **LIORF**                    |  |  |  |  |  |
| **DLIO**                     |  |  |  |  |  |
| **VineSLAM**                 |  |  |  |  |  |
| **KISS-ICP**                 |  |  |  |  |  |
| **GLIM**                     |  |  |  |  |  |
| **Kinematic-ICP**            |  |  |  |  |  |
| **MOLA-LO**                  |  |  |  |  |  |

## Relative Rotational Error (RRE)

Mean value calculated over all 10-meter segments. Values are presented in degrees per meter (°/m).

| 3D LiDAR Sensor              | Nav A Diff       | Nav A Omni       | Loop             | Slippage         | Ramp             |
| :--------------------------- | :--------------: | :--------------: | :--------------: | :--------------: | :--------------: |
| **A-LOAM**                   | 0.097 °/m | 0.084 °/m | 0.100 °/m | 0.084 °/m | 0.073 °/m |
| **LeGO-LOAM-BOR**            | 0.114 °/m | 0.104 °/m | 0.132 °/m | 0.114 °/m | 0.168 °/m |
| **LIORF**                    |  |  |  |  |  |
| **DLIO**                     |  |  |  |  |  |
| **VineSLAM**                 |  |  |  |  |  |
| **KISS-ICP**                 |  |  |  |  |  |
| **GLIM**                     |  |  |  |  |  |
| **Kinematic-ICP**            |  |  |  |  |  |
| **MOLA-LO**                  |  |  |  |  |  |

## Trajectory Plots