"""Areal reduction factor (logarithmic formulation)."""
from __future__ import annotations

import math


def arf_logarithmic(area_km2: float, k: float = 0.05) -> float:
    """ARF = 1 - k * log10(1 + area)."""
    if area_km2 <= 0:
        return 1.0
    return max(0.5, 1.0 - k * math.log10(1.0 + area_km2))
