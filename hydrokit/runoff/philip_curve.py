"""Philip two-term stepwise infiltration applier."""
from __future__ import annotations

from hydrokit.infiltration.philip import PhilipModel


def philip_effective(rain_series: list[float], step_hr: float, model: PhilipModel) -> list[float]:
    """Convert rainfall to effective excess."""
    out: list[float] = []
    t = step_hr  # avoid t=0 infinity
    for r in rain_series:
        capacity = model.rate(t) * step_hr
        out.append(max(0.0, r - capacity))
        t += step_hr
    return out
