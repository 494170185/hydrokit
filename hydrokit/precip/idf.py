"""Intensity-Duration-Frequency (IDF) curve.

i = A * (1 + C * log10 T) / (t + b) ^ n  (mm/min)
"""
from __future__ import annotations

import math


class IDFCurve:
    def __init__(self, a: float, c: float, b: float, n: float) -> None:
        if n <= 0 or n > 1.5:
            raise ValueError("n must be in (0, 1.5]")
        self.a = a
        self.c = c
        self.b = b
        self.n = n

    def intensity(self, duration_min: float, return_period_year: float) -> float:
        """Rainfall intensity (mm/min)."""
        if duration_min <= 0 or return_period_year <= 0:
            raise ValueError
        t = max(0.0, duration_min)
        return self.a * (1 + self.c * math.log10(return_period_year)) / (t + self.b) ** self.n

    def total_depth(self, duration_min: float, return_period_year: float) -> float:
        """Total depth (mm) over duration."""
        return self.intensity(duration_min, return_period_year) * duration_min
