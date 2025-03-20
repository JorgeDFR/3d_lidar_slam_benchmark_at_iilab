from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
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
    use_adaptive_threshold: bool = True
    fixed_threshold: float = 1.0 # Ignored if use_adaptive_threshold=true

    # Registration
    max_num_iterations: int = 10
    convergence_criterion: float = 0.001
    use_adaptive_odometry_regularization: bool = True
    fixed_regularization: float = 0.0 # Ignored if use_adaptive_odometry_regularization=true
    max_num_threads: int = 0

    # Covariance diagonal values
    position_covariance: float = 0.1
    orientation_covariance: float = 0.1

def generate_launch_description():
    # Launch Arguments
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

    # ROS topics and TF configuration
    use_2d_lidar = LaunchConfiguration("use_2d_lidar", default=False)
    lidar_topic = LaunchConfiguration("lidar_topic", default="/eve/ouster/points")
    wheel_odom_frame = LaunchConfiguration("wheel_odom_frame", default="eve/odom")
    base_frame = LaunchConfiguration("base_frame", default="eve/base_footprint")

    lidar_odometry_topic = LaunchConfiguration("lidar_odometry_topic", default="slam_odom")
    lidar_odom_frame = LaunchConfiguration("lidar_odom_frame", default="odom_lidar")
    publish_odom_tf = LaunchConfiguration("publish_odom_tf", default=True)
    invert_odom_tf = LaunchConfiguration("invert_odom_tf", default=True)

    # Common parameters for both nodes
    common_params = {
        "lidar_topic": lidar_topic,
        "use_2d_lidar": use_2d_lidar,
        "lidar_odom_frame": lidar_odom_frame,
        "wheel_odom_frame": wheel_odom_frame,
        "base_frame": base_frame,
        "publish_odom_tf": publish_odom_tf,
        "invert_odom_tf": invert_odom_tf,
        # Kinematic-ICP configuration
        "max_range": config.max_range,
        "min_range": config.min_range,
        "deskew": config.deskew,
        "max_points_per_voxel": config.max_points_per_voxel,
        "voxel_size": config.voxel_size,
        # Adaptive threshold
        "use_adaptive_threshold": config.use_adaptive_threshold,
        "fixed_threshold": config.fixed_threshold,
        # Registration
        "max_num_iterations": config.max_num_iterations,
        "convergence_criterion": config.convergence_criterion,
        "use_adaptive_odometry_regularization": config.use_adaptive_odometry_regularization,
        "fixed_regularization": config.fixed_regularization,
        # Fixed covariances
        "position_covariance": config.position_covariance,
        "orientation_covariance": config.orientation_covariance,
    }

    # Online node parameters
    online_params = common_params.copy()
    online_params.update({
        "tf_timeout": LaunchConfiguration("tf_timeout", default=0.1),
        "use_sim_time": LaunchConfiguration("use_sim_time", default=False),
    })

    # Offline node parameters
    offline_params = common_params.copy()
    offline_params.update({
        "tf_timeout": LaunchConfiguration("tf_timeout", default=0.0),
        "use_sim_time": LaunchConfiguration("use_sim_time", default=True),
        "bag_filename": LaunchConfiguration("rosbag_path"),
    })

    # Kinematic-ICP online node
    kinematic_icp_online_node = Node(
        package="kinematic_icp",
        executable="kinematic_icp_online_node",
        name="kinematic_icp_node",
        output="screen",
        remappings=[("lidar_odometry", lidar_odometry_topic),],
        parameters=[online_params],
        condition=UnlessCondition(LaunchConfiguration("run_offline"))
    )

    # Kinematic-ICP offline node
    kinematic_icp_offline_node = Node(
        package="kinematic_icp",
        executable="kinematic_icp_offline_node",
        name="kinematic_icp_node",
        output="screen",
        remappings=[("lidar_odometry", lidar_odometry_topic),],
        parameters=[offline_params],
        condition=IfCondition(LaunchConfiguration("run_offline"))
    )

    return LaunchDescription([
        run_offline_arg,
        rosbag_path_arg,
        kinematic_icp_online_node,
        kinematic_icp_offline_node,
    ])