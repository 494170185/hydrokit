"""General utilities."""
from __future__ import annotations


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def sign(v: float) -> int:
    return -1 if v < 0 else (1 if v > 0 else 0)


def safe_div(a: float, b: float, default: float = 0.0) -> float:
    return a / b if b != 0 else default


def trapezoid(xs: list[float], ys: list[float]) -> float:
    """Trapezoidal integral."""
    if len(xs) != len(ys) or len(xs) < 2:
        return 0.0
    return sum((xs[i + 1] - xs[i]) * (ys[i + 1] + ys[i]) / 2 for i in range(len(xs) - 1))


def interpolate(x: float, xs: list[float], ys: list[float]) -> float:
    """Linear interpolation."""
    if not xs:
        return 0.0
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            t = (x - xs[i]) / (xs[i + 1] - xs[i]) if xs[i + 1] != xs[i] else 0.5
            return ys[i] * (1 - t) + ys[i + 1] * t
    return ys[-1]
