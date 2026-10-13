"""
This module provides helpers for checking compatibility for certain functions depending on the current Maya API version and
the minimum target API version.
"""

from typing import Final, cast

from maya import cmds

MAYA_API_VERSION: Final[int] = cast("int", cmds.about(apiVersion=True))
TARGET_API_VERSION = 20242000


def current_and_target_compatible(version: int) -> bool:
    return (version <= MAYA_API_VERSION) and (version <= TARGET_API_VERSION)


def supports_shape_draw_on_top() -> bool:
    return current_and_target_compatible(20220000)
