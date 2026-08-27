"""Hydraulic jump (rectangular channel, conjugate depths)."""
from __future__ import annotations

import math

G = 9.81


def conjugate_depth_rectangular(y1: float, v1: float) -> float:
    """Conjugate depth y2 given (y1, v1) upstream. Uses Fr1."""
    if y1 <= 0 or v1 <= 0:
        raise ValueError
    fr1 = v1 / math.sqrt(G * y1)
    if fr1 <= 1:
        raise ValueError("fr1 must be > 1 (supercritical inflow)")
    return y1 / 2 * (math.sqrt(1 + 8 * fr1 * fr1) - 1)


def energy_loss_jump(y1: float, y2: float) -> float:
    """Specific energy loss (m) across jump."""
    if y1 <= 0 or y2 <= 0:
        raise ValueError
    return (y2 - y1) ** 3 / (4 * y1 * y2)
