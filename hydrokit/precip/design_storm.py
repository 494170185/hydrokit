"""Design storm pattern (Chicago method)."""
from __future__ import annotations

from hydrokit.precip.idf import IDFCurve


def chicago_hyetograph(
    curve: IDFCurve,
    duration_min: float,
    step_min: float,
    return_period_year: float,
    peak_coeff: float = 0.42,
) -> list[float]:
    """Return per-step depths (mm/step) with peak at peak_coeff * duration."""
    n = max(1, int(round(duration_min / step_min)))
    tp = peak_coeff * duration_min
    intensities: list[float] = []
    for i in range(n):
        t = (i + 0.5) * step_min
        # Chicago: intensity on each limb evaluated at duration = |t - tp|
        # smaller duration gives higher intensity → peak near tp
        d = abs(t - tp)
        d = max(step_min, d)
        i_r = curve.intensity(d, return_period_year)
        intensities.append(i_r)
    total = curve.total_depth(duration_min, return_period_year)
    s = sum(intensities) * step_min
    if s == 0:
        return [0.0] * n
    factor = total / s
    return [i * step_min * factor for i in intensities]
