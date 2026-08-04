"""Empirical frequency (plotting position) & moments."""
from __future__ import annotations

import math


def plotting_positions_weibull(values: list[float]) -> list[tuple[float, float]]:
    """Weibull formula: P = m/(n+1). Return [(value desc, P%)]."""
    s = sorted(values, reverse=True)
    n = len(s)
    return [(v, (i + 1) / (n + 1) * 100) for i, v in enumerate(s)]


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def std(values: list[float], sample: bool = True) -> float:
    n = len(values)
    if n < 2:
        return 0.0
    m = mean(values)
    var = sum((v - m) ** 2 for v in values) / (n - 1 if sample else n)
    return math.sqrt(var)


def cv(values: list[float]) -> float:
    m = mean(values)
    if m == 0:
        return 0.0
    return std(values) / m


def cs(values: list[float]) -> float:
    """Coefficient of skewness (sample)."""
    n = len(values)
    if n < 3:
        return 0.0
    m = mean(values)
    s = std(values)
    if s == 0:
        return 0.0
    return sum((v - m) ** 3 for v in values) * n / ((n - 1) * (n - 2) * s ** 3)
