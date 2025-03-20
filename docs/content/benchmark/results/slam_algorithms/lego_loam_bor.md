# LeGO-LOAM-BOR

## Absolute Trajectory Error (ATE)

Root Mean Square Error (RMSE) of the absolute position differences. Values are presented in meters (m).

| 3D LiDAR Sensor              | Nav A Diff     | Nav A Omni     | Loop           | Slippage       | Ramp           |
| :--------------------------- | :------------: | :------------: | :------------: | :------------: | :------------: |
| **Velodyne VLP-16**          | 0.054 m | 0.047 m | 0.042 m | 0.053 m | 0.050 m |
| **Ouster OS1-64**            | 0.042 m | 0.036 m | 0.033 m | 0.045 m | 0.036 m |
| **RoboSense RS-Helios-5515** | 0.040 m | 0.038 m | 0.039 m | 0.043 m | 0.041 m |
| **Livox Mid 360**            | - | - | - | - | - |

## Relative Translational Error (RTE)

Mean value calculated over all 10-meter segments. Values are presented as a percentage (%).

| 3D LiDAR Sensor              | Nav A Diff   | Nav A Omni   | Loop         | Slippage     | Ramp         |
| :--------------------------- | :----------: | :----------: | :----------: | :----------: | :----------: |
| **Velodyne VLP-16**          | 1.33% | 1.43% | 1.67% | 1.87% | 0.75% |
| **Ouster OS1-64**            | 1.14% | 1.23% | 1.43% | 1.44% | 0.52% |
| **RoboSense RS-Helios-5515** | 1.45% | 1.29% | 1.37% | 1.71% | 0.59% |
| **Livox Mid 360**            | - | - | - | - | - |

## Relative Rotational Error (RRE)

Mean value calculated over all 10-meter segments. Values are presented in degrees per meter (°/m).

| 3D LiDAR Sensor              | Nav A Diff       | Nav A Omni       | Loop             | Slippage         | Ramp             |
| :--------------------------- | :--------------: | :--------------: | :--------------: | :--------------: | :--------------: |
| **Velodyne VLP-16**          | 0.114 °/m | 0.110 °/m | 0.119 °/m | 0.151 °/m | 0.189 °/m |
| **Ouster OS1-64**            | 0.097 °/m | 0.106 °/m | 0.083 °/m | 0.104 °/m | 0.150 °/m |
| **RoboSense RS-Helios-5515** | 0.114 °/m | 0.104 °/m | 0.132 °/m | 0.114 °/m | 0.168 °/m |
| **Livox Mid 360**            | - | - | - | - | - |

## Trajectory Plots
