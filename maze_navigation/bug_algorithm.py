# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from sensor_msgs.msg import LaserScan

# class BugAlgorithm(Node):
#     def __init__(self):
#         super().__init__('bug_algorithm')
#         self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
#         self.sub = self.create_subscription(LaserScan, 'scan', self.scan_callback, 10)
#         self.get_logger().info("BugAlgorithm node started")

#     def scan_callback(self, msg):
#         # simple placeholder: stop robot if obstacle very close
#         twist = Twist()
#         if min(msg.ranges) < 0.5:
#             twist.linear.x = 0.0
#         else:
#             twist.linear.x = 0.2
#         self.pub.publish(twist)

# def main(args=None):
#     rclpy.init(args=args)
#     node = BugAlgorithm()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
