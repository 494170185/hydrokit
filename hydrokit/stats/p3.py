"""P-III (Pearson type III) distribution, commonly used in CN hydrology.

X_p = mean * (1 + cv * K_p), K_p ~ standardized P-III deviate.
Wilson-Hilferty transform for upper tail approximation.
"""
from __future__ import annotations

from hydrokit.stats.frequency import cs as calc_cs, cv as calc_cv, mean
from hydrokit.stats.normal import normal_ppf


def kp_from_p(cs_val: float, p: float) -> float:
    """Standardized P-III deviate K_p at exceedance probability p (0-1)."""
    if cs_val == 0:
        return normal_ppf(1 - p)
    t = normal_ppf(1 - p)
    term = (1 - cs_val ** 2 / 24) ** 3
    kf = (2 / cs_val) * ((1 + cs_val * t / 6 - cs_val ** 2 / 36) ** 3 - term)
    return kf


def design_value(values: list[float], p: float, cs_ratio: float | None = None) -> float:
    """Return P-III design value at probability p (0-1 exceedance)."""
    mu = mean(values)
    c = calc_cv(values)
    if cs_ratio is not None:
        s = c * cs_ratio
    else:
        s = calc_cs(values)
    kp = kp_from_p(s, p)
    return mu * (1 + c * kp)
