# Usage

The benchmark process involves the following steps:

1. Download the IILABS 3D dataset
2. Set up the Docker environment
3. Run SLAM algorithms on the dataset
4. Evaluate the results

## Download the IILABS 3D Dataset

The IILABS 3D dataset is available at the [INESC TEC research data repository](https://rdm.inesctec.pt/dataset/nis-2025-001). You can download it manually or use the IILABS 3D toolkit for easier access.

### Using the IILABS 3D Toolkit

The [IILABS 3D Toolkit](https://github.com/JorgeDFR/iilabs3d-toolkit) provides utilities for working with the dataset.

#### Installation

```bash
pip install iilabs3d-toolkit
```

!!! tip "Autocompletion"
    You can install autocompletion for the toolkit by running:
    ```bash
    iilabs3d --install-completion
    ```
    Restart your shell for the autocompletion to take effect.

#### Downloading Sequences

To download a specific sequence for a specific sensor:

```bash
iilabs3d download <output_directory> <sequence_name> <sensor_name>
```

For example, to download the *loop* benchmark sequence for the Livox Mid-360 sensor:

```bash
iilabs3d download ~/slam_data loop livox_mid_360
```

To download all benchmark sequences for all sensors:

```bash
iilabs3d download ~/slam_data bench all
```

!!! info "Dataset Structure"
    The sequences will be saved in the following structure:
    ```
    <output_directory>/iilabs3d-dataset/<sequence_prefix>/<sensor_name>/<sequence_name>/
    ```

!!! tip "Dataset Directory"
    The provided Docker Compose file is configured to mount the `${HOME}/slam_data` directory, allowing containerized access to the dataset files. To ensure proper functionality, save your dataset in this directory. Alternatively, you can modify the `docker-compose.yml` file to specify a different path if needed.

## Set Up the Docker Environment

The benchmark uses Docker to ensure a consistent environment for all SLAM algorithms. This approach guarantees reproducibility and simplifies the setup process.

### Prerequisites

- :material-docker: [Docker](https://docs.docker.com/get-docker/) installed on your system
- :material-harddisk: At least 10GB of free disk space
- :material-memory: 16GB RAM recommended for optimal performance

!!! info "Guide for installing Docker and other tools in Ubuntu 20.04"
    For more detailed information about the Docker installation and additional setups, please refer to the [Install Docker](benchmark/install_docker.md) section.

### Clone the Repository

```bash
git clone https://github.com/JorgeDFR/3d_lidar_slam_benchmark_at_iilab.git
cd 3d_lidar_slam_benchmark_at_iilab/docker
```

### Build and Run Docker Containers

The benchmark uses two Docker images. You can either build the images locally from the provided Dockerfiles (slower, compiles libraries/packages) or pull prebuilt images from Docker Hub (faster).

=== "ROS 1 (Noetic)"
    Contains the following SLAM algorithms:
    
    - :octicons-check-circle-fill-24: A-LOAM
    - :octicons-check-circle-fill-24: LeGO-LOAM-BOR
    - :octicons-check-circle-fill-24: LIORF
    - :octicons-check-circle-fill-24: DLIO

    #### Option 1: Pull Prebuilt Image

    ```bash
    docker pull jorgedfr/3d_slam_ros1:noetic
    ```

    #### Option 2: Build Image Locally

    ```bash
    docker compose build ros1_noetic
    ```

    #### Start Docker Container

    ```bash
    docker compose up ros1_noetic -d
    ```

    #### Access Docker Container

    ```bash
    docker exec -it 3d_slam_ros1 bash
    ```

=== "ROS 2 (Humble)"
    Contains the following SLAM algorithms:
     
    - :octicons-check-circle-fill-24: VineSLAM
    - :octicons-check-circle-fill-24: KISS-ICP
    - :octicons-check-circle-fill-24: GLIM
    - :octicons-check-circle-fill-24: Kinematic-ICP
    - :octicons-check-circle-fill-24: MOLA-LO

    #### Option 1: Pull Prebuilt Image

    ```bash
    docker pull jorgedfr/3d_slam_ros2:humble
    ```

    #### Option 2: Build Image Locally

    ```bash
    docker compose build ros2_humble
    ```

    #### Start Docker Container

    ```bash
    docker compose up ros2_humble -d
    ```

    #### Access Docker Container

    ```bash
    docker exec -it 3d_slam_ros2 bash
    ```

!!! warning "GUI Applications"
    Before running RViz inside the Docker container, you need to set up `xhost`:
    ```bash
    ./setup_xhost.sh
    ```

## Run SLAM Algorithms on the Dataset

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

### Offline Processing Mode

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

## Record and Evaluate Results

### Recording Odometry Trajectories

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
    For MOLA-LO, set an environment variable to use the LiDAR frame instead of the default `base_link` frame. This step is necessary because MOLA-LO expects the robot frame to be `base_link`, while the IILABS 3D dataset uses `eve/base_link`. Then use the `mola-lidar-odometry-cli` command. For more informations regarding this tool please refer to the [MOLA](https://docs.mola-slam.org/latest/mola_lo_apps.html) main documentation.
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

### Converting to TUM Format

Now, to convert the odometry trajectory to TUM format, you can use the evo toolkit, which is automatically installed along with the IILABS 3D toolkit:

=== "ROS 1 (Noetic)"

    ```bash
    evo_traj bag <rosbag_file_path> slam_odom --save_as_tum
    ```

=== "ROS 2 (Humble)"

    ```bash
    evo_traj bag2 <rosbag_file_path> slam_odom --save_as_tum
    ```

### Evaluating Trajectories

Use the IILABS 3D toolkit to evaluate the trajectory against the ground truth:

```bash
iilabs3d eval <ground_truth.tum> <odometry.tum>
```

This will calculate metrics including Absolute Trajectory Error (ATE), Relative Translational Error (RTE), and Relative Rotational Error (RRE).