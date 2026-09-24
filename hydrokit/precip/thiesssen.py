"""Thiessen polygon computation (requires geometry)."""
from __future__ import annotations


def thiessen_weights(points: list[tuple[float, float]]) -> list[float]:
    """Rough area weights by nearest neighbor distance (placeholder).

    Real Thiessen requires Voronoi diagram; use precomputed polygon areas
    via `hydrokit.precip.spatial.thiessen_weights` for production use.
    """
    if not points:
        return []
    return [1.0 / len(points)] * len(points)
