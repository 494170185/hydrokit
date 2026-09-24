"""Extra math helpers."""
from __future__ import annotations

import math


def exp_decay(series: list[float], k: float) -> list[float]:
    """e^{-k t} attenuated series."""
    return [v * math.exp(-k * i) for i, v in enumerate(series)]


def growth_curve(series: list[float], k: float) -> list[float]:
    """1 - e^{-k t} saturating series."""
    return [v * (1 - math.exp(-k * i)) for i, v in enumerate(series)]


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def weighted_mean(values: list[float], weights: list[float]) -> float:
    if not values or len(values) != len(weights):
        return 0.0
    s = sum(weights)
    if s == 0:
        return 0.0
    return sum(v * w for v, w in zip(values, weights)) / s
