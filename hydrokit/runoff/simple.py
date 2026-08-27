"""Simple runoff coefficient method."""
from __future__ import annotations


def runoff_depth_coefficient(precip_mm: float, runoff_coeff: float) -> float:
    """Runoff depth = C * P. C in [0, 1]."""
    if not 0 <= runoff_coeff <= 1:
        raise ValueError("runoff_coeff in [0, 1]")
    return precip_mm * runoff_coeff


def runoff_series(precip_series: list[float], runoff_coeff: float) -> list[float]:
    return [runoff_depth_coefficient(p, runoff_coeff) for p in precip_series]
