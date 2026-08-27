"""Priestley-Taylor potential evapotranspiration."""
from __future__ import annotations

from hydrokit.evap.penman import psychrometric_constant, slope_vapor_pressure_curve


def priestley_taylor(t_mean: float, rn_mj_m2: float, elevation_m: float, alpha: float = 1.26) -> float:
    """ET (mm/day). α typically 1.26 (well-watered)."""
    delta = slope_vapor_pressure_curve(t_mean)
    gamma = psychrometric_constant(elevation_m)
    return alpha * delta / (delta + gamma) * 0.408 * rn_mj_m2
