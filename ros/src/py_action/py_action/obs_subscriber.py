import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class ObsSubscriber(Node):
    def __init__(self):
        super().__init__('obs_subscriber')
        self.subscription = self.create_subscription(String, 'topic', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    sub = ObsSubscriber()
    rclpy.spin(sub)
    
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
