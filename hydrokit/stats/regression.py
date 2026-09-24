"""Simple linear regression."""
from __future__ import annotations


def linregress(xs: list[float], ys: list[float]) -> tuple[float, float, float]:
    """Return (slope, intercept, r_squared)."""
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    slope = num / den if den else 0.0
    intercept = my - slope * mx
    # R²
    ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys)
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    return slope, intercept, r2


def log_linear_regress(xs: list[float], ys: list[float]) -> tuple[float, float, float]:
    """log10-linear fit."""
    import math
    xs_log = [math.log10(x) for x in xs if x > 0]
    ys_log = [math.log10(y) for y in ys if y > 0]
    n = min(len(xs_log), len(ys_log))
    return linregress(xs_log[:n], ys_log[:n])
