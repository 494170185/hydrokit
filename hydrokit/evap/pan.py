"""Pan evaporation coefficient method."""
from __future__ import annotations


def pan_to_lake_evaporation(pan_mm: float, k_pan: float = 0.7) -> float:
    """Lake/pond evaporation ≈ K_p * E_pan. K_p typically 0.6-0.8 (Class A)."""
    if pan_mm < 0:
        raise ValueError
    if not 0 < k_pan <= 1:
        raise ValueError("k_pan in (0, 1]")
    return pan_mm * k_pan


def pan_to_et0(pan_mm: float, k_pan: float = 0.85) -> float:
    """Reference ET0 from Class A pan."""
    return pan_mm * k_pan
