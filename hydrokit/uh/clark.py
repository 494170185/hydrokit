"""Clark IUH: linear reservoir behind time-area translation."""
from __future__ import annotations

import math


def clark_iuh(tc_hr: float, r_hr: float, step_hr: float, duration_hr: float = 5.0) -> tuple[list[float], list[float]]:
    """Clark instantaneous UH (dimensionless normalized), then translate by tc.

    Simplified: treats translation as pure lag of tc_r, attenuation as linear reservoir R.
    Returns (times_hr, ordinates normalized to unit depth).
    """
    if r_hr <= 0:
        raise ValueError("r_hr must be positive")
    n = max(5, int(duration_hr / step_hr))
    times: list[float] = []
    qs: list[float] = []
    for i in range(n):
        t = i * step_hr
        if t < tc_hr:
            q = 0.0
        else:
            q = math.exp(-(t - tc_hr) / r_hr) / r_hr
        times.append(t)
        qs.append(q)
    # normalize to unit volume over 1 hour step
    area = sum(qs) * step_hr
    if area > 0:
        qs = [q / area for q in qs]
    return times, qs
