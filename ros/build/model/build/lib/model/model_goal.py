import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_state.action import Jointstate


class ModelGoal(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Jointstate, 'jointstate')

    def send_goal(self, order):
        goal_msg = True
        self._action_client.wait_for_server()

        return self._action_client.send_goal_async(goal_msg)
    
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    action_client = ModelGoal()

    future = action_client.send_goal(True)

    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()