import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SetEntityState
from gazebo_msgs.msg import EntityState
import math
import random
import time

class MultiObstaclePublisher(Node):
    def __init__(self):
        super().__init__('multi_obstacle_publisher')
        
        self.client = self.create_client(SetEntityState, '/set_entity_state')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        time.sleep(1)
        
        self.timer = self.create_timer(0.01, self.timer_callback)
        self.last_time = self.get_clock().now()
        
        self.obstacles = [
            {
                'model_name': 'moving_obstacle_1',
                'position': [-1.0, 2.275, 0.1],
                'velocity': [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), 0.0]
            },
            {
                'model_name': 'moving_obstacle_2',
                'position': [-3.2, 2.2, 0.1],
                'velocity': [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), 0.0]
            }
        ]
        self.bounds = {'x': (-4.3, -0.1), 'y': (0.1, 9.4)}
    
    def timer_callback(self):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        # Move each obstacle
        for obs in self.obstacles:
            pos = obs['position']
            vel = obs['velocity']
            new_pos = [
                pos[0] + vel[0] * dt,
                pos[1] + vel[1] * dt,
                pos[2]
            ]
            
            if new_pos[0] < self.bounds['x'][0] or new_pos[0] > self.bounds['x'][1]:
                vel[0] = -vel[0]
                new_pos[0] = pos[0] + vel[0] * dt
            if new_pos[1] < self.bounds['y'][0] or new_pos[1] > self.bounds['y'][1]:
                vel[1] = -vel[1]
                new_pos[1] = pos[1] + vel[1] * dt

            obs['new_position'] = new_pos
            obs['velocity'] = vel

        # Send updated states
        for obs in self.obstacles:
            state = EntityState()
            state.name = obs['model_name']
            state.pose.position.x = obs['new_position'][0]
            state.pose.position.y = obs['new_position'][1]
            state.pose.position.z = obs['new_position'][2]
            state.pose.orientation.w = 1.0
            state.reference_frame = 'world'

            request = SetEntityState.Request()
            request.state = state

            future = self.client.call_async(request)
            future.add_done_callback(lambda f: None)

            obs['position'] = obs['new_position']

def main(args=None):
    rclpy.init(args=args)
    node = MultiObstaclePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
