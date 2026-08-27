"""Penman-Monteith FAO-56 reference evapotranspiration."""
from __future__ import annotations

import math


def saturation_vapor_pressure_kpa(t_celsius: float) -> float:
    """FAO-56 Eq. 11."""
    return 0.6108 * math.exp(17.27 * t_celsius / (t_celsius + 237.3))


def slope_vapor_pressure_curve(t_celsius: float) -> float:
    """Δ kPa/°C. FAO-56 Eq. 13."""
    es = saturation_vapor_pressure_kpa(t_celsius)
    return 4098 * es / (t_celsius + 237.3) ** 2


def psychrometric_constant(elevation_m: float) -> float:
    """γ in kPa/°C. FAO-56 Eq. 8."""
    p = 101.3 * ((293 - 0.0065 * elevation_m) / 293) ** 5.26
    return 0.665e-3 * p


def penman_monteith_daily(
    tmin: float, tmax: float,
    rs_mj_m2: float,
    rh_mean: float,
    u2_m_s: float,
    elevation_m: float,
    rn_mj_m2: float | None = None,
) -> float:
    """ET0 mm/day. rn default: approximate 0.77 * rs - 2.0."""
    if rs_mj_m2 < 0 or rh_mean < 0 or rh_mean > 100 or u2_m_s < 0:
        raise ValueError
    tmean = (tmin + tmax) / 2
    delta = slope_vapor_pressure_curve(tmean)
    gamma = psychrometric_constant(elevation_m)
    es = (saturation_vapor_pressure_kpa(tmin) + saturation_vapor_pressure_kpa(tmax)) / 2
    ea = es * rh_mean / 100.0
    rn = rn_mj_m2 if rn_mj_m2 is not None else max(0.0, 0.77 * rs_mj_m2 - 2.0)
    num = 0.408 * delta * rn + gamma * (900 / (tmean + 273)) * u2_m_s * (es - ea)
    den = delta + gamma * (1 + 0.34 * u2_m_s)
    return num / den
