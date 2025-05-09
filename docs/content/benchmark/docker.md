# Docker Environment

To ensure reproducibility and consistency in the benchmarking process, we provide a Docker environment that contains all the necessary dependencies and configurations for running the SLAM algorithms. This Docker environment allows researchers to easily replicate our benchmarking results and test their own algorithms under the same conditions.

## Docker Images

The benchmark uses two Docker images:

=== "ROS 1 Image"
    Contains the following SLAM algorithms:
    
    - :octicons-check-circle-fill-24: A-LOAM
    - :octicons-check-circle-fill-24: LeGO-LOAM-BOR
    - :octicons-check-circle-fill-24: LIORF
    - :octicons-check-circle-fill-24: DLIO

=== "ROS 2 Image"
    Contains the following SLAM algorithms:
    
    - :octicons-check-circle-fill-24: VineSLAM
    - :octicons-check-circle-fill-24: KISS-ICP
    - :octicons-check-circle-fill-24: GLIM
    - :octicons-check-circle-fill-24: Kinematic-ICP
    - :octicons-check-circle-fill-24: MOLA-LO

Both images include:

- :material-eye: Visualization tools including RViz
- :material-file-document: All necessary dependencies and configurations

## Installation

### Prerequisites

- :material-docker: [Docker](https://docs.docker.com/get-docker/) installed on your system
- :material-harddisk: At least 10GB of free disk space
- :material-memory: 16GB RAM recommended for optimal performance

!!! info "Guide for installing Docker and other tools in Ubuntu 20.04"
    For more detailed information about the Docker installation and additional setups, please refer to the [Install Docker](install_docker.md) section.

### Setup Instructions

Clone the repository:

```bash
git clone https://github.com/JorgeDFR/3d_lidar_slam_benchmark_at_iilab.git
cd 3d_lidar_slam_benchmark_at_iilab/docker
```

=== "ROS 1 (Noetic)"

    #### Option 1: Pull Prebuilt Image (faster)

    ```bash
    docker pull jorgedfr/3d_slam_ros1:noetic
    ```

    #### Option 2: Build Image Locally (slower)

    ```bash
    docker compose build ros1_noetic
    ```

    Start the Docker container:

    ```bash
    docker compose up ros1_noetic -d
    ```

    Access the Docker container:

    ```bash
    docker exec -it 3d_slam_ros1 bash
    ```

=== "ROS 2 (Humble)"

    #### Option 1: Pull Prebuilt Image (faster)

    ```bash
    docker pull jorgedfr/3d_slam_ros2:humble
    ```

    #### Option 2: Build Image Locally (slower)

    ```bash
    docker compose build ros2_humble
    ```

    Start the Docker container:

    ```bash
    docker compose up ros2_humble -d
    ```

    Access the Docker container:

    ```bash
    docker exec -it 3d_slam_ros2 bash
    ```

!!! warning "GUI Applications"
    Before running RViz inside the Docker container, you need to set up `xhost`:
    ```bash
    ./setup_xhost.sh
    ```

!!! warning "Dataset Directory"
    The provided Docker Compose file is configured to mount the `${HOME}/slam_data` directory, allowing containerized access to the dataset files. To ensure proper functionality, save your dataset in this directory. Alternatively, you can modify the `docker-compose.yml` file to specify a different path if needed.
    
## Running SLAM Algorithms

=== "ROS 1 (Noetic)"

    In one terminal, set the enviroment variables to select the algorithm and 3D LiDAR sensor, and start the SLAM algorithm:

    ```bash
    # Set environment variables
    export SLAM_CONF=<algorithm_name>  
    # Options: aloam, lego_loam_bor, liorf, dlio

    export SLAM_SENSOR=<sensor_name>  
    # Options: velodyne_vlp_16, ouster_os1_64, robosense_rs_helios_5515, livox_mid_360

    # Start the SLAM algorithm
    roslaunch slam_benchmark_ros1_conf slam_benchmark.launch
    ```

    In another terminal, play the rosbag of the desired sequence:

    ```bash
    rosbag play <rosbag_file_path>
    ```

=== "ROS 2 (Humble)"

    In one terminal, set the enviroment variables to select the algorithm and 3D LiDAR sensor, and start the SLAM algorithm:

    ```bash
    # Set environment variables
    export SLAM_CONF=<algorithm_name>  
    # Options: vineslam, kiss_icp, glim, kinematic_icp, mola_lo

    export SLAM_SENSOR=<sensor_name>  
    # Options: velodyne_vlp_16, ouster_os1_64, robosense_rs_helios_5515, livox_mid_360

    # Start the SLAM algorithm
    ros2 launch slam_benchmark_ros2_conf slam_benchmark.launch.xml
    ```
    In another terminal, play the rosbag of the desired sequence:

    ```bash
    ros2 bag play <rosbag_file_path>
    ```

!!! warning "VineSLAM Special Case"
    VineSLAM requires recompilation of its ROS 2 package whenever the LiDAR sensor is changed. Use the `-DLIDAR_TYPE` CMake argument to specify your sensor:

    - `-DLIDAR_TYPE=0` (default) for Velodyne VLP-16
    - `-DLIDAR_TYPE=1` for RoboSense RS-Helios-5515
    - `-DLIDAR_TYPE=3` for Ouster-OS1-64
    - `-DLIDAR_TYPE=4` for Livox Mid-360

    ```bash
    cd ros2_ws
    colcon build --packages-select vineslam_ros --cmake-args -DLIDAR_TYPE=0
    ```
    
## Offline Processing Mode

Alternatively, several SLAM algorithms support an offline mode that processes rosbag files faster than real-time without losing messages:

=== "ROS 1 (Noetic)"

    ```bash
    roslaunch slam_benchmark_ros1_conf slam_benchmark.launch run_offline:=true rosbag_path:=<rosbag_file_path>
    ```

=== "ROS 2 (Humble)"

    ```bash
    ros2 launch slam_benchmark_ros2_conf slam_benchmark.launch.xml run_offline:=true rosbag_path:=<rosbag_file_path>
    ```

!!! note "Supported Algorithms for Offline Mode"
    The following algorithms currently support offline processing:
    
    - LeGO-LOAM-BOR
    - GLIM
    - Kinematic-ICP
    - MOLA-LO

## Recording Odometry Trajectories

To record the odometry trajectory generated by the SLAM algorithms, run the following command in another terminal:

=== "ROS 1 (Noetic)"

    ```bash
    rosbag record -O <output_bag_file_name> /slam_odom
    ```

=== "ROS 2 (Humble)"

    ```bash
    ros2 bag record -o <output_bag_file_name> /slam_odom
    ```

!!! warning "MOLA-LO Special Case"
    For MOLA-LO, use the following command:
    ```bash
    # Set environment variable to use the LiDAR frame instead of base_link
    export MOLA_USE_FIXED_LIDAR_POSE=true
    
    mola-lidar-odometry-cli \
        -c $(ros2 pkg prefix mola_lidar_odometry)/share/mola_lidar_odometry/pipelines/lidar3d-default.yaml \
        --input-rosbag2 <path_to_bag_file> \
        --lidar-sensor-label <lidar_topic> \
        --output-tum-path <output_file_path>
    ```
    
    - `<path_to_bag_file>`: Path to your input rosbag file
    - `<lidar_topic>`: LiDAR sensor topic name (`/eve/ouster/points` for Ouster sequences or `/eve/lidar3d` for other sensors)
    - `<output_file_path>`: Desired path for the TUM-formatted trajectory output