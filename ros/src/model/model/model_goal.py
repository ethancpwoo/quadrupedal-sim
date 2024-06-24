import rclpy
import serial 
import time

from rclpy.action import ActionClient
from rclpy.node import Node

from action_state.action import Jointstate


class ModelGoal(Node):

    def __init__(self):
        super().__init__('model_action_client')
        self._action_client = ActionClient(self, Jointstate, 'jointstate')
        self.iters = 0
        self.s = serial.Serial(port='/dev/ttyACM1', baudrate=9600)
        while(1):
            self.s.flush()
            self.s.write(b'10010000000')
            res = self.s.readline()
            if (res.strip().decode() == 'configed'):
                self.s.flush()
                break

    def send_goal(self):
        goal_msg = Jointstate.Goal()
        goal_msg.result = True
        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)
    
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
        self.get_logger().info('Result: {0}'.format(result.jointactions))
        for i in result.jointactions:
            print(i)
            self.s.write(str(i).encode() + b'\n')
        time.sleep(0.1)
        self.send_goal()
        self.iters += 1
        if self.iters == 250:
          rclpy.shutdown()


def main(args=None):
    
    rclpy.init(args=args)

    action_client = ModelGoal()

    action_client.send_goal()

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()