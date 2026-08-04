"""Spatial distribution (point-to-area reduction)."""
from __future__ import annotations


def area_reduction_factor(area_km2: float) -> float:
    """USWB / WMO simple: ARF = 1 - C * a^p (a in km²)."""
    if area_km2 <= 0:
        return 1.0
    c = 0.01
    p = 0.2
    arf = 1.0 - c * area_km2 ** p
    return max(0.3, min(1.0, arf))


def thiessen_weights(polygon_areas: list[float]) -> list[float]:
    total = sum(polygon_areas)
    if total <= 0:
        return [0.0] * len(polygon_areas)
    return [a / total for a in polygon_areas]


def areal_mean(rainfalls: list[float], weights: list[float]) -> float:
    return sum(r * w for r, w in zip(rainfalls, weights))
