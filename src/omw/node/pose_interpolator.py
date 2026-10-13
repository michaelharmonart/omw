from omw.attribute import (
    ArrayAttribute,
    BooleanAttribute,
    DoubleAttribute,
    EnumAttribute,
    FloatAttribute,
    IntegerAttribute,
    LongAttribute,
    PoseInterpolatorDirectoryAttribute,
    PoseInterpolatorPoseAttribute,
)
from omw.attribute.pose_interpolator import PoseInterpolatorDriverAttribute
from omw.enum import PoseInterpolatorInterpolation

from .core import Node


class PoseInterpolatorNode(Node):
    node_type = "poseInterpolator"
    plugin = "poseInterpolator"

    def __init__(self, name: str = "poseInterpolator") -> None:
        super().__init__(name)

    def _setup_attributes(self) -> None:
        self.allow_negative_weights = BooleanAttribute(f"{self.name}.allowNegativeWeights")
        self.display_output = BooleanAttribute(f"{self.name}.displayOutput")
        self.display_spacing = DoubleAttribute(f"{self.name}.displaySpacing")
        self.driver = ArrayAttribute(f"{self.name}.driver", PoseInterpolatorDriverAttribute)
        self.enable_rotation = BooleanAttribute(f"{self.name}.enableRotation")
        self.enable_translation = BooleanAttribute(f"{self.name}.enableTranslation")
        self.interpolation = EnumAttribute(
            f"{self.name}.interpolation", PoseInterpolatorInterpolation
        )
        self.mid_layer_id = IntegerAttribute(f"{self.name}.midLayerId")
        self.mid_layer_parent = LongAttribute(f"{self.name}.midLayerParent")
        self.next_node = LongAttribute(f"{self.name}.nextNode")
        self.output = ArrayAttribute(f"{self.name}.output", FloatAttribute)
        self.output_smoothing = FloatAttribute(f"{self.name}.outputSmoothing")
        self.pose = ArrayAttribute(f"{self.name}.pose", PoseInterpolatorPoseAttribute)
        self.regularization = DoubleAttribute(f"{self.name}.regularization")


class PoseInterpolatorManagerNode(Node):
    """Maya poseInterpolatorManager node with enhanced interface."""

    node_type = "poseInterpolatorManager"
    plugin = "poseInterpolator"

    def __init__(self, name: str = "poseInterpolatorManager") -> None:
        super().__init__(name)

    def _setup_attributes(self) -> None:
        self.pose_interpolator_directory = ArrayAttribute(
            f"{self.name}.poseInterpolatorDirectory", PoseInterpolatorDirectoryAttribute
        )
        self.pose_interpolator_parent = ArrayAttribute(
            f"{self.name}.poseInterpolatorParent", LongAttribute
        )
