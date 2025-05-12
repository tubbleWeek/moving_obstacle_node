Taken from CSCI5551 Final Project

To run with the default world
```
ros2 launch moving_obstacle_node moving_obstacle.launch.py
```

You can take the boilerplate code and modify it for as many obstacles as you want

### Notes
Each world needs the `<plugin name='gazebo_ros_state' filename='libgazebo_ros_state.so'/>` line in if for the obstacles to move, and you need to launch gazebo with `libgazebo_ros_state.so` active.

This was tested in Gazebo Classic in ROS Humble
