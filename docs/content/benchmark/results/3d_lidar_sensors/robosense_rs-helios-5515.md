# RoboSense RS-Helios-5515

## Absolute Trajectory Error (ATE)

Root Mean Square Error (RMSE) of the absolute position differences. Values are presented in meters (m).

| 3D LiDAR Sensor              | Nav A Diff     | Nav A Omni     | Loop           | Slippage       | Ramp           |
| :--------------------------- | :------------: | :------------: | :------------: | :------------: | :------------: |
| **A-LOAM**                   | 0.032 m        | 0.032 m        | 0.045 m        | 0.042 m        | 0.057 m        |
| **LeGO-LOAM-BOR**            | 0.040 m        | 0.038 m        | 0.039 m        | 0.043 m        | 0.041 m        |
| **LIORF**                    | <u>0.029</u> m | <u>0.024</u> m | <u>0.023</u> m | <u>0.029</u> m | 0.034 m        |
| **DLIO**                     | 0.068 m        | 0.050 m        | 0.040 m        | 0.074 m        | <u>0.030</u> m |
| **VineSLAM**                 | 0.108 m        | 0.078 m        | 0.123 m        | 0.095 m        | 0.056 m        |
| **KISS-ICP**                 | 0.046 m        | 0.046 m        | 0.047 m        | 0.041 m        | 0.039 m        |
| **GLIM**                     | 0.137 m        | 0.055 m        | 0.560 m        | 0.030 m        | 0.057 m        |
| **Kinematic-ICP**            | 0.337 m        | 0.178 m        | 0.103 m        | 0.676 m        | -              |
| **MOLA-LO**                  | 0.044 m        | 0.031 m        | 0.032 m        | 0.040 m        | 0.134 m        |

## Relative Translational Error (RTE)

Mean value calculated over all 10-meter segments. Values are presented as a percentage (%).

| 3D LiDAR Sensor              | Nav A Diff   | Nav A Omni   | Loop         | Slippage     | Ramp         |
| :--------------------------- | :----------: | :----------: | :----------: | :----------: | :----------: |
| **A-LOAM**                   | <u>0.92</u>% | <u>1.05</u>% | 1.03%        | 1.32%        | 0.59%        |
| **LeGO-LOAM-BOR**            | 1.45%        | 1.29%        | 1.37%        | 1.71%        | 0.59%        |
| **LIORF**                    | 1.23%        | 1.24%        | 1.28%        | 0.97%        | 0.47%        |
| **DLIO**                     | 1.55%        | 1.64%        | 1.36%        | 1.31%        | <u>0.30</u>% |
| **VineSLAM**                 | 2.00%        | 1.97%        | 2.55%        | 1.67%        | 0.80%        |
| **KISS-ICP**                 | 1.10%        | 1.10%        | <u>1.00</u>% | <u>0.96</u>% | 0.58%        |
| **GLIM**                     | 1.60%        | 1.16%        | 7.36%        | 1.43%        | 0.65%        |
| **Kinematic-ICP**            | 2.87%        | 2.27%        | 1.62%        | 8.86%        | -            |
| **MOLA-LO**                  | 1.26%        | 1.15%        | 1.25%        | 1.21%        | 0.94%        |

## Relative Rotational Error (RRE)

Mean value calculated over all 10-meter segments. Values are presented in degrees per meter (°/m).

| 3D LiDAR Sensor              | Nav A Diff       | Nav A Omni       | Loop             | Slippage         | Ramp             |
| :--------------------------- | :--------------: | :--------------: | :--------------: | :--------------: | :--------------: |
| **A-LOAM**                   | 0.097 °/m        | 0.084 °/m        | 0.100 °/m        | 0.084 °/m        | 0.073 °/m        |
| **LeGO-LOAM-BOR**            | 0.114 °/m        | 0.104 °/m        | 0.132 °/m        | 0.114 °/m        | 0.168 °/m        |
| **LIORF**                    | 0.090 °/m        | 0.109 °/m        | 0.093 °/m        | 0.077 °/m        | 0.119 °/m        |
| **DLIO**                     | 0.107 °/m        | 0.122 °/m        | 0.102 °/m        | 0.073 °/m        | 0.125 °/m        |
| **VineSLAM**                 | 0.148 °/m        | 0.177 °/m        | 0.199 °/m        | 0.111 °/m        | 0.315 °/m        |
| **KISS-ICP**                 | 0.091 °/m        | 0.080 °/m        | 0.098 °/m        | 0.081 °/m        | 0.125 °/m        |
| **GLIM**                     | <u>0.051</u> °/m | <u>0.038</u> °/m | <u>0.049</u> °/m | <u>0.038</u> °/m | <u>0.036</u> °/m |
| **Kinematic-ICP**            | 0.184 °/m        | 0.143 °/m        | 0.118 °/m        | 0.110 °/m        | -                |
| **MOLA-LO**                  | 0.104 °/m        | 0.076 °/m        | 0.104 °/m        | 0.099 °/m        | 0.230 °/m        |

## Trajectory Plots