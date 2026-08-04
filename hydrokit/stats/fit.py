"""Fit quality: error metrics."""
from __future__ import annotations

import math


def rmse(sample: list[float], curve: list[float]) -> float:
    if len(sample) != len(curve) or not sample:
        return float("inf")
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(sample, curve)) / len(sample))


def bias(sample: list[float], curve: list[float]) -> float:
    if not sample:
        return float("inf")
    return sum(a - b for a, b in zip(sample, curve)) / len(sample)
