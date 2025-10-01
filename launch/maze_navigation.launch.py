from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Path to your maze world
    maze_world_path = os.path.join(
        os.getenv("HOME"), "maze_ws/src/maze_navigation/worlds/maze_world.sdf"
    )

    # TurtleBot3 Gazebo launch
    turtlebot3_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory("turtlebot3_gazebo"),
                "launch",
                "turtlebot3_world.launch.py"
            )
        ]),
        launch_arguments={"world": maze_world_path}.items()
    )

    # Your navigation algorithm node
    bug_algorithm_node = Node(
        package="maze_navigation",
        executable="bug_algorithm.py",
        output="screen"
    )

    return LaunchDescription([
        turtlebot3_gazebo,
        bug_algorithm_node
    ])
