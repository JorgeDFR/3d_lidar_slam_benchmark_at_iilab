import os
from launch import LaunchDescription
from launch_ros.actions import Node

# Comamnd to build the package for different LiDAR models:
# colcon build --packages-select vineslam_ros --cmake-args -DLIDAR_TYPE=1

# The -DLIDAR_TYPE cmake argument compiles VineSLAM for specific LiDAR sensors:
# -DLIDAR_TYPE=0 corresponds to Velodyne VLP-16
# -DLIDAR_TYPE=1 corresponds to RoboSense RS-Helios-5515
# -DLIDAR_TYPE=2 corresponds to Livox Mid 70
# -DLIDAR_TYPE=3 corresponds to Ouster-OS1-64
# -DLIDAR_TYPE=4 uses all the features of the subscribed point cloud
# The default value is 0, if no -DLIDAR_TYPE is chosen

def generate_launch_description():
    dirname, _ = os.path.split(os.path.realpath(__file__))
    params = os.path.join(dirname, 'vineslam_iilabs3d_robosense_rs_helios_5515.yaml')

    ld = LaunchDescription()

    # VineSLAM node
    vineslam = Node(
        package='vineslam_ros',
        executable='slam_node',
        name='slam_node',
        parameters=[params],
        remappings=[
            ('scan_topic', '/eve/lidar3d'),
            ('odom_topic', '/eve/odom'),
            ('imu_data_topic', '/eve/imu/data'),
            ('/vineslam/pose', '/slam_odom'),

            # ('gps_topic', '/fix'),
            # ('gps_heading_topic', '/navrelposned'),
            # ('imu_topic', '/imu/rpy'),
        ],
    )
    ld.add_action(vineslam)

    return ld