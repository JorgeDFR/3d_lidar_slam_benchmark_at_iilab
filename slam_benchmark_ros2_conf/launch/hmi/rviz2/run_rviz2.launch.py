from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d", LaunchConfiguration("rviz_file")]
    )

    return LaunchDescription([rviz_node])