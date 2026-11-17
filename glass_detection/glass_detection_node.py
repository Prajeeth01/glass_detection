#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
from vision_msgs.msg import Detection3DArray


def contains_glass(msg: Detection3DArray) -> bool:
    """
    Check if glass is detected.

    :param msg: Detection3DArray containing detected objects.
    :return: True if glass is detected, otherwise False.
    """
    for detection in msg.detections:
        if not detection.results:
            continue

        result = detection.results[0]

        if not hasattr(result, "hypothesis"):
            continue

        class_id = result.hypothesis.class_id

        if class_id.lower() == "glass":
            return True

    return False


class GlassDetectionNode(Node):
    """ROS2 node for detecting glass objects."""

    def __init__(self) -> None:
        """Initialize the Glass Detection node."""
        super().__init__("glass_detection_node")

        self.glass_publisher = self.create_publisher(
            Bool,
            "glass_detected",
            10,
        )

        self.subscription = self.create_subscription(
            Detection3DArray,
            "detections",
            self.object_callback,
            10,
        )

        self.get_logger().info("Glass Detection Node Started")

    def object_callback(
        self,
        msg: Detection3DArray,
    ) -> None:
        """
        Process incoming detection messages.

        :param msg: Detection3DArray containing detections.
        """
        glass_detected = contains_glass(msg)

        result_msg = Bool()
        result_msg.data = glass_detected

        self.glass_publisher.publish(result_msg)

        self.get_logger().info(f"Glass detected: {glass_detected}")


def main(args: list[str] | None = None) -> None:
    """
    Start the Glass Detection ROS2 node.

    :param args: Command line arguments.
    """
    rclpy.init(args=args)

    node = GlassDetectionNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
