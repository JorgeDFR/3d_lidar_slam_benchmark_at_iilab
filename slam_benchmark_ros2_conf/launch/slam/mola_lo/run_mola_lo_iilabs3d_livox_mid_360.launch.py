import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription, SetEnvironmentVariable, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Declare launch arguments
    run_offline_arg = DeclareLaunchArgument(
        'run_offline',
        default_value='false',
        description='Run in offline mode (true for rosbag playback)'
    )
    rosbag_path_arg = DeclareLaunchArgument(
        'rosbag_path',
        default_value='',
        description='Path to the rosbag file'
    )

    # Launch configuration variables
    run_offline = LaunchConfiguration('run_offline')
    rosbag_path = LaunchConfiguration('rosbag_path')

    # Offline mode actions: set environment variables and execute the rosbag node
    offline_actions = [
        SetEnvironmentVariable('MOLA_LIDAR_TOPIC', '/eve/lidar3d'),
        SetEnvironmentVariable('MOLA_USE_FIXED_LIDAR_POSE', 'true'),
        ExecuteProcess(
            cmd=['mola-lo-gui-rosbag2', rosbag_path],
            output='screen'
        )
    ]

    # Online mode: include the lidar odometry launch file using PathJoinSubstitution
    online_launch_file = PathJoinSubstitution(
        [FindPackageShare('mola_lidar_odometry'), 'ros2-launchs', 'ros2-lidar-odometry.launch.py']
    )

    online_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(online_launch_file),
        launch_arguments={
            'lidar_topic_name': '/eve/lidar3d',
            'ignore_lidar_pose_from_tf': 'true',
            'publish_localization_following_rep105': 'false',
            'use_rviz': 'false'
        }.items()
    )

    # Build the launch description with conditional groups
    ld = LaunchDescription()
    ld.add_action(run_offline_arg)
    ld.add_action(rosbag_path_arg)
    ld.add_action(GroupAction(
        actions=offline_actions,
        condition=IfCondition(run_offline)
    ))
    ld.add_action(GroupAction(
        actions=[online_include],
        condition=UnlessCondition(run_offline)
    ))

    return ld
