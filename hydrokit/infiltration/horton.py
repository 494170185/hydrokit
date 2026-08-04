"""Horton infiltration model.

f(t) = fc + (f0 - fc) * exp(-k t)
"""
from __future__ import annotations

import math


class HortonModel:
    def __init__(self, f0: float, fc: float, k: float) -> None:
        """f0/fc in mm/hr, k in 1/hr."""
        if f0 < fc:
            raise ValueError("f0 must be >= fc")
        if k <= 0:
            raise ValueError("k must be positive")
        self.f0 = f0
        self.fc = fc
        self.k = k

    def rate(self, t_hr: float) -> float:
        """Instantaneous infiltration rate at t (hr)."""
        return self.fc + (self.f0 - self.fc) * math.exp(-self.k * t_hr)

    def cumulative(self, t_hr: float) -> float:
        """Cumulative infiltration F(t) (mm)."""
        return self.fc * t_hr + (self.f0 - self.fc) / self.k * (1 - math.exp(-self.k * t_hr))


def effective_rainfall_horton(
    rain_mm_hr: list[float],
    step_hr: float,
    model: HortonModel,
) -> list[float]:
    """Apply Horton to a hyetograph: return excess rainfall (mm) per step."""
    excess: list[float] = []
    t = 0.0
    for r in rain_mm_hr:
        capacity = model.rate(t) * step_hr
        exc = max(0.0, r - capacity)
        excess.append(exc)
        t += step_hr
    return excess
