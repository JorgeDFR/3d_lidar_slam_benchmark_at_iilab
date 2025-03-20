# Velodyne VLP-16

## Absolute Trajectory Error (ATE)

Root Mean Square Error (RMSE) of the absolute position differences. Values are presented in meters (m).

| 3D LiDAR Sensor              | Nav A Diff     | Nav A Omni     | Loop           | Slippage       | Ramp           |
| :--------------------------- | :------------: | :------------: | :------------: | :------------: | :------------: |
| **A-LOAM**                   | 0.031 m | 0.049 m | 0.039 m | 0.040 m | 0.031 m |
| **LeGO-LOAM-BOR**            | 0.054 m | 0.047 m | 0.042 m | 0.053 m | 0.050 m |
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
| **A-LOAM**                   | 1.28% | 1.58% | 1.68% | 1.53% | 0.38% |
| **LeGO-LOAM-BOR**            | 1.33% | 1.43% | 1.67% | 1.87% | 0.75% |
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
| **A-LOAM**                   | 0.066 °/m | 0.084 °/m | 0.104 °/m | 0.083 °/m | 0.072 °/m |
| **LeGO-LOAM-BOR**            | 0.114 °/m | 0.110 °/m | 0.119 °/m | 0.151 °/m | 0.189 °/m |
| **LIORF**                    |  |  |  |  |  |
| **DLIO**                     |  |  |  |  |  |
| **VineSLAM**                 |  |  |  |  |  |
| **KISS-ICP**                 |  |  |  |  |  |
| **GLIM**                     |  |  |  |  |  |
| **Kinematic-ICP**            |  |  |  |  |  |
| **MOLA-LO**                  |  |  |  |  |  |

## Trajectory Plots