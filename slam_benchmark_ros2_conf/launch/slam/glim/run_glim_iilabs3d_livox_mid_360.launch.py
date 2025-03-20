import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node

def generate_launch_description():
    dirname, _ = os.path.split(os.path.realpath(__file__))
    config_path = os.path.join(dirname, "config_iilabs3d/livox_mid_360")
    # config_path = os.path.join(dirname, "config_iilabs3d/livox_mid_360_internal_imu")

    run_offline_arg = DeclareLaunchArgument(
        "run_offline",
        default_value="false",
        description="If true, run offline (using rosbag). Otherwise, run online."
    )

    rosbag_path_arg = DeclareLaunchArgument(
        "rosbag_path",
        default_value="",
        description="Path to the rosbag file (used only in offline mode)"
    )

    # GLIM online node
    glim_ros_online_node = Node(
        package="glim_ros",
        executable="glim_rosnode",
        name="glim_rosnode",
        output="screen",
        parameters=[{"config_path": config_path}],
        remappings=[("glim_rosnode/odom", "slam_odom")],
        condition=UnlessCondition(LaunchConfiguration("run_offline"))
    )

     # GLIM offline node
    glim_ros_offline_node = Node(
        package="glim_ros",
        executable="glim_rosbag",
        name="glim_rosnode",
        output="screen",
        arguments=[LaunchConfiguration("rosbag_path")],
        parameters=[{"config_path": config_path}],
        remappings=[("glim_rosnode/odom", "slam_odom")],
        condition=IfCondition(LaunchConfiguration("run_offline"))
    )

    return LaunchDescription([
        run_offline_arg,
        rosbag_path_arg,
        glim_ros_online_node,
        glim_ros_offline_node,
    ])