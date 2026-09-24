"""Mainstream slope estimation."""
from __future__ import annotations


def slope_10_85(elevations: list[float], distances: list[float]) -> float:
    """Slope between 10% and 85% of mainstream (Taylor-Schwarz).

    elevations = elevation along channel at increasing distance from outlet.
    distances = channel distance from outlet.
    """
    if len(elevations) != len(distances) or len(elevations) < 2:
        raise ValueError
    n = len(elevations)
    i_low = int(0.10 * (n - 1))
    i_high = max(i_low + 1, int(0.85 * (n - 1)))
    dz = elevations[i_high] - elevations[i_low]
    dx = distances[i_high] - distances[i_low]
    if dx <= 0:
        raise ValueError("distances must be increasing")
    return dz / dx


def mean_slope(elevations: list[float], distances: list[float]) -> float:
    if len(elevations) != len(distances) or len(elevations) < 2:
        raise ValueError
    return (elevations[-1] - elevations[0]) / (distances[-1] - distances[0])
