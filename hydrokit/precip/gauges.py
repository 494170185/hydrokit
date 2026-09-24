"""Rain gauge station modeling."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Gauge:
    id: str
    name: str
    x_km: float
    y_km: float
    elevation_m: float = 0.0


def distance(g1: Gauge, g2: Gauge) -> float:
    return ((g1.x_km - g2.x_km) ** 2 + (g1.y_km - g2.y_km) ** 2) ** 0.5


def idw(target: tuple[float, float], gauges: list[Gauge], values: list[float], power: float = 2.0) -> float:
    """Inverse-distance-weighted estimate at target point."""
    if len(gauges) != len(values):
        raise ValueError
    if not gauges:
        return 0.0
    weights: list[float] = []
    for g in gauges:
        d = ((g.x_km - target[0]) ** 2 + (g.y_km - target[1]) ** 2) ** 0.5
        if d == 0:
            return values[gauges.index(g)]
        weights.append(1.0 / (d ** power))
    s = sum(weights)
    if s == 0:
        return 0.0
    return sum(w * v for w, v in zip(weights, values)) / s
