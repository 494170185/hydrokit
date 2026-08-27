"""Manning's open-channel flow."""
from __future__ import annotations

import math


def manning_q(r_m: float, s0: float, n: float, area_m2: float) -> float:
    """Q = (1/n) * A * R^(2/3) * sqrt(S0). Returns m^3/s."""
    if n <= 0 or area_m2 <= 0 or s0 < 0:
        raise ValueError
    return (1.0 / n) * area_m2 * (r_m ** (2 / 3)) * math.sqrt(s0)


def manning_v(r_m: float, s0: float, n: float) -> float:
    """V = (1/n) R^(2/3) sqrt(S0) m/s."""
    if n <= 0 or s0 < 0:
        raise ValueError
    return (1.0 / n) * (r_m ** (2 / 3)) * math.sqrt(s0)


def hydraulic_radius_rectangular(width_m: float, depth_m: float) -> float:
    if width_m <= 0 or depth_m <= 0:
        raise ValueError
    area = width_m * depth_m
    wetted = width_m + 2 * depth_m
    return area / wetted


def hydraulic_radius_trapezoid(bottom_width_m: float, depth_m: float, side_slope: float) -> float:
    """Trapezoid with side slope z:1 (horizontal:vertical)."""
    if bottom_width_m <= 0 or depth_m <= 0:
        raise ValueError
    b, y, z = bottom_width_m, depth_m, side_slope
    area = (b + z * y) * y
    wetted = b + 2 * y * math.sqrt(1 + z * z)
    return area / wetted
