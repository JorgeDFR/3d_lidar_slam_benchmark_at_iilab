from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

class config:
    # Preprocessing
    max_range: float = 100.0
    min_range: float = 0.3
    deskew: bool = False

    # Mapping parameters
    voxel_size: float = 1.0
    max_points_per_voxel: int = 20

    # Adaptive threshold
    initial_threshold: float = 2.0
    min_motion_th: float = 0.1

    # Registration
    max_num_iterations: int = 500
    convergence_criterion: float = 0.0001
    max_num_threads: int = 0

    # Covariance diagonal values
    position_covariance: float = 0.1
    orientation_covariance: float = 0.1

def generate_launch_description():
    # ROS configuration
    visualize = LaunchConfiguration("visualize", default=True)
    use_sim_time = LaunchConfiguration("use_sim_time", default=False)

    # ROS topics and TF configuration
    pointcloud_topic = LaunchConfiguration("topic", default="eve/lidar3d")
    base_frame = LaunchConfiguration("base_frame", default="eve/base_link")

    odom_topic = LaunchConfiguration("odom_topic", default="slam_odom")
    lidar_odom_frame = LaunchConfiguration("lidar_odom_frame", default="odom_lidar")
    publish_odom_tf = LaunchConfiguration("publish_odom_tf", default=True)
    invert_odom_tf = LaunchConfiguration("invert_odom_tf", default=True)

    # KISS-ICP node
    kiss_icp_node = Node(
        package="kiss_icp",
        executable="kiss_icp_node",
        name="kiss_icp_node",
        output="screen",
        remappings=[
            ("pointcloud_topic", pointcloud_topic),
            ("kiss/odometry", odom_topic),
        ],
        parameters=[
            {
                # ROS node configuration
                "base_frame": base_frame,
                "lidar_odom_frame": lidar_odom_frame,
                "publish_odom_tf": publish_odom_tf,
                "invert_odom_tf": invert_odom_tf,
                # KISS-ICP configuration
                "max_range": config.max_range,
                "min_range": config.min_range,
                "deskew": config.deskew,
                "max_points_per_voxel": config.max_points_per_voxel,
                "voxel_size": config.voxel_size,
                # Adaptive threshold
                "initial_threshold": config.initial_threshold,
                "min_motion_th": config.min_motion_th,
                # Registration
                "max_num_iterations": config.max_num_iterations,
                "convergence_criterion": config.convergence_criterion,
                "max_num_threads": config.max_num_threads,
                # Fixed covariances
                "position_covariance": config.position_covariance,
                "orientation_covariance": config.orientation_covariance,
                # ROS CLI arguments
                "publish_debug_clouds": visualize,
                "use_sim_time": use_sim_time,
            },
        ],
    )

    return LaunchDescription([kiss_icp_node])