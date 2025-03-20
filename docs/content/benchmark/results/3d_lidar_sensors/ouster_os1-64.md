# Ouster OS1-64

## Absolute Trajectory Error (ATE)

Root Mean Square Error (RMSE) of the absolute position differences. Values are presented in meters (m).

| 3D LiDAR Sensor              | Nav A Diff     | Nav A Omni     | Loop           | Slippage       | Ramp           |
| :--------------------------- | :------------: | :------------: | :------------: | :------------: | :------------: |
| **A-LOAM**                   | 0.039 m | 0.043 m | 0.029 m | 0.041 m | 0.038 m |
| **LeGO-LOAM-BOR**            | 0.042 m | 0.036 m | 0.033 m | 0.045 m | 0.036 m |
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
| **A-LOAM**                   | 1.11% | 1.34% | 1.15% | 1.18% | 0.39% |
| **LeGO-LOAM-BOR**            | 1.14% | 1.23% | 1.43% | 1.44% | 0.52% |
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
| **A-LOAM**                   | 0.072 °/m | 0.089 °/m | 0.080 °/m | 0.088 °/m | 0.052 °/m |
| **LeGO-LOAM-BOR**            | 0.097 °/m | 0.106 °/m | 0.083 °/m | 0.104 °/m | 0.150 °/m |
| **LIORF**                    |  |  |  |  |  |
| **DLIO**                     |  |  |  |  |  |
| **VineSLAM**                 |  |  |  |  |  |
| **KISS-ICP**                 |  |  |  |  |  |
| **GLIM**                     |  |  |  |  |  |
| **Kinematic-ICP**            |  |  |  |  |  |
| **MOLA-LO**                  |  |  |  |  |  |

## Trajectory Plots