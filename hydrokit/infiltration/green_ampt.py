"""Green-Ampt infiltration model.

f = K * (1 + psi * delta_theta / F)
F is cumulative infiltration, psi = suction head, delta_theta = saturation deficit.
"""
from __future__ import annotations

import math


class GreenAmptModel:
    def __init__(self, k: float, psi: float, delta_theta: float) -> None:
        """k in mm/hr, psi in mm, delta_theta dimensionless."""
        if k <= 0 or psi < 0 or delta_theta <= 0:
            raise ValueError
        self.k = k
        self.psi = psi
        self.dtheta = delta_theta

    def rate(self, cumulative_mm: float) -> float:
        if cumulative_mm <= 0:
            return float("inf")
        return self.k * (1 + self.psi * self.dtheta / cumulative_mm)

    def time_to_ponding(self, rainfall_intensity_mm_hr: float) -> float:
        """Time when infiltration capacity drops below rainfall intensity."""
        if rainfall_intensity_mm_hr <= self.k:
            return float("inf")
        # F_p = K * psi * dtheta / (i - K)
        fp = self.k * self.psi * self.dtheta / (rainfall_intensity_mm_hr - self.k)
        # Solve fp = K*t + psi*dtheta*ln(1 + fp/(psi*dtheta)) iteratively
        t = fp / rainfall_intensity_mm_hr
        for _ in range(20):
            t_new = (fp - self.psi * self.dtheta * math.log(1 + fp / (self.psi * self.dtheta))) / self.k
            if abs(t_new - t) < 1e-6:
                break
            t = t_new
        return max(t, 0.0)
