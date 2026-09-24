"""Design rainfall depth extraction from IDF."""
from __future__ import annotations

from hydrokit.precip.idf import IDFCurve


def design_depth_at(curve: IDFCurve, durations_min: list[float], t_year: float) -> dict[float, float]:
    """Return {duration_min: depth_mm} for a given return period."""
    return {d: curve.total_depth(d, t_year) for d in durations_min}


def standard_durations() -> list[float]:
    """CN GB standard durations (min)."""
    return [5, 10, 15, 20, 30, 45, 60, 90, 120, 180, 360, 720, 1440]
