import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('moving_obstacle_node')
    urdf_file = os.path.join(pkg_share, 'urdf', 'obstacle.urdf')
    
    world_file = os.path.join(pkg_share, 'worlds', 'world.world')
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'moving_obstacle_1',
            '-file', urdf_file,
            '-x', '0', '-y', '0', '-z', '0.5',

        ],
        output='screen'
    )
    spawn_entity_2 = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'moving_obstacle_2',
                '-file', urdf_file,
                '-x', '0', '-y', '0', '-z', '0.5',

            ],
            output='screen'
        )
    moving_obstacle_publisher = Node(
        package='moving_obstacle_node',
        executable='obstacles',
        output='screen'
    )
    return LaunchDescription([
        ExecuteProcess(
        cmd=[
            'gazebo', '--verbose', world_file,
            '-s', 'libgazebo_ros_init.so',
            '-s', 'libgazebo_ros_factory.so',
            '-s', 'libgazebo_ros_force_system.so'
        ],
        output='screen'
        ),
        spawn_entity,
        spawn_entity_2,
        moving_obstacle_publisher
    ])
