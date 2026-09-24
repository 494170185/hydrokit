"""Meteorological input container + validators."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MetDaily:
    tmin: float
    tmax: float
    rs_mj_m2: float
    rh_mean: float
    u2_m_s: float
    elevation_m: float

    def validate(self) -> None:
        if self.tmin > self.tmax:
            raise ValueError("tmin > tmax")
        if not 0 <= self.rh_mean <= 100:
            raise ValueError("rh_mean")
        if self.rs_mj_m2 < 0:
            raise ValueError("rs_mj_m2")
        if self.u2_m_s < 0:
            raise ValueError("u2_m_s")
