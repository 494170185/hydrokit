"""Pure lag (translation) routing."""
from __future__ import annotations


def lag(inflow: list[float], lag_steps: int) -> list[float]:
    """Shift series right by `lag_steps`, padding front with zeros."""
    if lag_steps < 0:
        raise ValueError
    return [0.0] * lag_steps + list(inflow)


def attenuate(inflow: list[float], alpha: float) -> list[float]:
    """First-order exponential smoothing. alpha in (0, 1]."""
    if not 0 < alpha <= 1:
        raise ValueError
    if not inflow:
        return []
    out = [inflow[0]]
    for x in inflow[1:]:
        out.append(alpha * x + (1 - alpha) * out[-1])
    return out
