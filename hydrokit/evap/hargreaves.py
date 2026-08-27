"""Hargreaves-Samani temperature-based ET0."""
from __future__ import annotations

import math


def extraterrestrial_radiation(lat_deg: float, day_of_year: int) -> float:
    """MJ/m²/day. FAO-56 Eq. 21."""
    phi = math.radians(lat_deg)
    dr = 1 + 0.033 * math.cos(2 * math.pi * day_of_year / 365)
    ds = 0.409 * math.sin(2 * math.pi * day_of_year / 365 - 1.39)
    ws = math.acos(max(-1.0, min(1.0, -math.tan(phi) * math.tan(ds))))
    gsc = 0.0820
    return (24 * 60 / math.pi) * gsc * dr * (ws * math.sin(phi) * math.sin(ds) +
            math.cos(phi) * math.cos(ds) * math.sin(ws))


def hargreaves(tmean: float, tmin: float, tmax: float, lat_deg: float, day_of_year: int) -> float:
    """ET0 mm/day."""
    if tmax < tmin:
        raise ValueError("tmax < tmin")
    ra = extraterrestrial_radiation(lat_deg, day_of_year)
    temp_range = max(0.0, tmax - tmin)
    return 0.0023 * (tmean + 17.8) * math.sqrt(temp_range) * ra * 0.408
