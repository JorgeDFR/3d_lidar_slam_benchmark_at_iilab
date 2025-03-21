# MOLA-LO

## Absolute Trajectory Error (ATE)

Root Mean Square Error (RMSE) of the absolute position differences. Values are presented in meters (m).

| 3D LiDAR Sensor              | Nav A Diff     | Nav A Omni     | Loop           | Slippage       | Ramp           |
| :--------------------------- | :------------: | :------------: | :------------: | :------------: | :------------: |
| **Velodyne VLP-16**          | 0.045 m        | 0.040 m        | 0.037 m        | 0.039 m        | 0.338 m        |
| **Ouster OS1-64**            | 0.028 m        | 0.026 m        | 0.020 m        | 0.028 m        | <u>0.015</u> m |
| **RoboSense RS-Helios-5515** | 0.044 m        | 0.031 m        | 0.032 m        | 0.040 m        | 0.134 m        |
| **Livox Mid-360**            | <u>0.025</u> m | <u>0.022</u> m | <u>0.018</u> m | <u>0.027</u> m | 0.023 m        |

## Relative Translational Error (RTE)

Mean value calculated over all 10-meter segments. Values are presented as a percentage (%).

| 3D LiDAR Sensor              | Nav A Diff   | Nav A Omni   | Loop         | Slippage     | Ramp         |
| :--------------------------- | :----------: | :----------: | :----------: | :----------: | :----------: |
| **Velodyne VLP-16**          | 1.41%        | 1.48%        | 1.69%        | 1.54%        | 3.53%        |
| **Ouster OS1-64**            | 0.97%        | 1.07%        | 1.06%        | 1.12%        | <u>0.24</u>% |
| **RoboSense RS-Helios-5515** | 1.26%        | 1.15%        | 1.25%        | 1.21%        | 0.94%        |
| **Livox Mid-360**            | <u>0.77</u>% | <u>0.77</u>% | <u>0.98</u>% | <u>0.93</u>% | 0.26%        |

## Relative Rotational Error (RRE)

Mean value calculated over all 10-meter segments. Values are presented in degrees per meter (°/m).

| 3D LiDAR Sensor              | Nav A Diff       | Nav A Omni       | Loop             | Slippage         | Ramp             |
| :--------------------------- | :--------------: | :--------------: | :--------------: | :--------------: | :--------------: |
| **Velodyne VLP-16**          | 0.088 °/m        | 0.088 °/m        | 0.106 °/m        | 0.092 °/m        | 0.822 °/m        |
| **Ouster OS1-64**            | 0.070 °/m        | 0.080 °/m        | <u>0.057</u> °/m | 0.064 °/m        | <u>0.054</u> °/m |
| **RoboSense RS-Helios-5515** | 0.104 °/m        | 0.076 °/m        | 0.104 °/m        | 0.099 °/m        | 0.230 °/m        |
| **Livox Mid-360**            | <u>0.057</u> °/m | <u>0.063</u> °/m | 0.058 °/m        | <u>0.047</u> °/m | 0.056 °/m        |

## Trajectory Plots

### Nav A Diff Sequence 
<div class="grid" markdown>
![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_nav_a_diff_velodyne.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_nav_a_diff_ouster.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_nav_a_diff_robosense.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_nav_a_diff_livox.png)
</div>

### Nav A Omni Sequence 
<div class="grid" markdown>
![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_nav_a_omni_velodyne.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_nav_a_omni_ouster.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_nav_a_omni_robosense.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_nav_a_omni_livox.png)
</div>

### Loop Sequence 
<div class="grid" markdown>
![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_loop_velodyne.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_loop_ouster.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_loop_robosense.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_loop_livox.png)
</div>

### Slippage Sequence 
<div class="grid" markdown>
![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_slippage_velodyne.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_slippage_ouster.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_slippage_robosense.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_slippage_livox.png)
</div>

### Ramp Sequence 
<div class="grid" markdown>
![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_ramp_velodyne.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_ramp_ouster.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_ramp_robosense.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_ramp_livox.png)
</div>

### Elevator Sequence 
<div class="grid" markdown>
![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_elevator_velodyne.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_elevator_ouster.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_elevator_robosense.png)

![](../../../../assets/results/slam_algorithms/mola_lo/mola_lo_elevator_livox.png)
</div>