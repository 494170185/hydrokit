"""Temporal distribution patterns."""
from __future__ import annotations

import math


def uniform_pattern(depth_mm: float, n_steps: int) -> list[float]:
    return [depth_mm / n_steps] * n_steps


def triangular_pattern(depth_mm: float, n_steps: int, peak_fraction: float = 0.5) -> list[float]:
    if n_steps < 2:
        return [depth_mm]
    pk = max(1, min(n_steps - 1, int(round(n_steps * peak_fraction))))
    rising = [(i + 0.5) / pk for i in range(pk)]
    falling = [(n_steps - i - 0.5) / (n_steps - pk) for i in range(pk, n_steps)]
    weights = rising + falling
    s = sum(weights)
    return [w / s * depth_mm for w in weights]


def gaussian_pattern(x: float, mu: float, sigma: float) -> float:
    return math.exp(-((x - mu) ** 2) / (2 * sigma * sigma))


def scs_type_ii(n_steps: int) -> list[float]:
    """Approximate SCS Type II weights (normalized)."""
    if n_steps < 3:
        return [1.0 / n_steps] * n_steps
    weights = [gaussian_pattern((i + 0.5) / n_steps, 0.5, 0.10) for i in range(n_steps)]
    s = sum(weights)
    return [w / s for w in weights]
