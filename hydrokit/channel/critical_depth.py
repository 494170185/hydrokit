"""Critical depth: dE/dy = 0 → Fr = 1."""
from __future__ import annotations

import math

G = 9.81  # m/s²


def critical_depth_rectangular(q_m3s: float, width_m: float) -> float:
    """yc = (Q² / (g * B²))^(1/3)."""
    if q_m3s <= 0 or width_m <= 0:
        raise ValueError
    return ((q_m3s ** 2) / (G * width_m ** 2)) ** (1 / 3)


def critical_depth_trapezoid(
    q_m3s: float, b_m: float, side_slope: float,
    tol: float = 1e-4, max_iter: int = 80,
) -> float:
    """Solve for y such that Fr = 1 in trapezoidal channel."""
    if q_m3s <= 0 or b_m < 0:
        raise ValueError

    def fr_minus_one(y: float) -> float:
        area = (b_m + side_slope * y) * y
        top = b_m + 2 * side_slope * y
        if area <= 0 or top <= 0:
            return -1.0
        v = q_m3s / area
        v_c = math.sqrt(G * area / top)
        return v / v_c - 1.0

    # expand hi until sign change (fr_minus_one: supercritical → subcritical as y grows)
    hi = 0.1
    for _ in range(60):
        if fr_minus_one(hi) < 0:
            break
        hi *= 2.0
    lo = 0.001
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        if fr_minus_one(mid) > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2


def froude(v: float, g_l: float, characteristic_length: float) -> float:
    return v / math.sqrt(g_l * max(characteristic_length, 1e-9))
