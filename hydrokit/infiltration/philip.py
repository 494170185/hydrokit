"""Philip two-term infiltration.

f(t) = 0.5 * S * t^-0.5 + K
F(t) = S * sqrt(t) + K * t
"""
from __future__ import annotations

import math


class PhilipModel:
    def __init__(self, sorptivity: float, conductivity: float) -> None:
        """S in mm/hr^0.5, K in mm/hr."""
        if sorptivity < 0:
            raise ValueError
        self.S = sorptivity
        self.K = conductivity

    def rate(self, t_hr: float) -> float:
        if t_hr <= 0:
            return float("inf")
        return 0.5 * self.S / math.sqrt(t_hr) + self.K

    def cumulative(self, t_hr: float) -> float:
        if t_hr <= 0:
            return 0.0
        return self.S * math.sqrt(t_hr) + self.K * t_hr
