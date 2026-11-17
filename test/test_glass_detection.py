"""Tests for the Glass Detection ROS 2 node."""

from unittest.mock import MagicMock, patch

import rclpy
from rclpy.executors import SingleThreadedExecutor
from std_msgs.msg import Bool
from vision_msgs.msg import Detection3D, Detection3DArray, ObjectHypothesisWithPose

from glass_detection import glass_detection_node
from glass_detection.glass_detection_node import (
    GlassDetectionNode,
    contains_glass,
)


def create_detection(class_id: str) -> Detection3D:
    """Create a fake detection message."""
    detection = Detection3D()

    hypothesis = ObjectHypothesisWithPose()
    hypothesis.hypothesis.class_id = class_id

    detection.results.append(hypothesis)

    return detection


def create_detection_array(class_id: str) -> Detection3DArray:
    """Create a fake detection array."""
    message = Detection3DArray()
    message.detections.append(create_detection(class_id))

    return message


def test_contains_glass_true() -> None:
    """Verify glass detection returns true for glass class."""
    message = create_detection_array("glass")

    assert contains_glass(message) is True


def test_contains_glass_false() -> None:
    """Verify glass detection returns false for non glass class."""
    message = create_detection_array("person")

    assert contains_glass(message) is False


def test_node_creation_and_spin_up() -> None:
    """Verify ROS node starts and spins."""
    if not rclpy.ok():
        rclpy.init()

    node = GlassDetectionNode()
    executor = SingleThreadedExecutor()

    executor.add_node(node)

    try:
        executor.spin_once(timeout_sec=0.2)

        assert node.get_name() == "glass_detection_node"

    finally:
        executor.remove_node(node)
        node.destroy_node()
        executor.shutdown()

        if rclpy.ok():
            rclpy.shutdown()


def test_object_callback_publishes_true() -> None:
    """Verify callback publishes true for glass."""
    if not rclpy.ok():
        rclpy.init()

    node = GlassDetectionNode()
    message = create_detection_array("glass")

    try:
        with patch.object(
            node.glass_publisher,
            "publish",
        ) as mock_publish:

            node.object_callback(message)

        published = mock_publish.call_args.args[0]

        assert isinstance(published, Bool)
        assert published.data is True

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


def test_object_callback_publishes_false() -> None:
    """Verify callback publishes false for non glass."""
    if not rclpy.ok():
        rclpy.init()

    node = GlassDetectionNode()
    message = create_detection_array("person")

    try:
        with patch.object(
            node.glass_publisher,
            "publish",
        ) as mock_publish:

            node.object_callback(message)

        published = mock_publish.call_args.args[0]

        assert isinstance(published, Bool)
        assert published.data is False

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


def test_main() -> None:
    """Verify main initializes, spins, and shuts down."""
    fake_node = MagicMock()

    with patch.object(
        glass_detection_node,
        "GlassDetectionNode",
        return_value=fake_node,
    ), patch.object(
        glass_detection_node.rclpy,
        "init",
    ) as mock_init, patch.object(
        glass_detection_node.rclpy,
        "spin",
    ) as mock_spin, patch.object(
        glass_detection_node.rclpy,
        "shutdown",
    ) as mock_shutdown:

        glass_detection_node.main()

    mock_init.assert_called_once()
    mock_spin.assert_called_once_with(fake_node)
    fake_node.destroy_node.assert_called_once()
    mock_shutdown.assert_called_once()
