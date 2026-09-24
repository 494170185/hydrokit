"""Cross-section library: rect / trapezoid / circular."""
from __future__ import annotations

import math


def rect_area(b: float, y: float) -> float:
    return b * y


def rect_top_width(b: float, y: float) -> float:
    return b


def rect_wetted_perimeter(b: float, y: float) -> float:
    return b + 2 * y


def trap_area(b: float, y: float, z: float) -> float:
    return (b + z * y) * y


def trap_top_width(b: float, y: float, z: float) -> float:
    return b + 2 * z * y


def trap_wetted_perimeter(b: float, y: float, z: float) -> float:
    return b + 2 * y * math.sqrt(1 + z * z)


def circular_area(d: float, y: float) -> float:
    """Partially filled circular pipe."""
    if y <= 0:
        return 0.0
    if y >= d:
        return math.pi * d * d / 4
    r = d / 2
    theta = 2 * math.acos(1 - y / r)
    return (r ** 2 / 2) * (theta - math.sin(theta))


def circular_wetted_perimeter(d: float, y: float) -> float:
    if y <= 0:
        return 0.0
    if y >= d:
        return math.pi * d
    r = d / 2
    theta = 2 * math.acos(1 - y / r)
    return r * theta
