"""Gumbel (EV1) distribution."""
from __future__ import annotations

import math

from hydrokit.stats.frequency import mean, std


def gumbel_fit(values: list[float]) -> tuple[float, float]:
    """Method of moments → (loc, scale)."""
    sigma = std(values)
    if sigma == 0:
        return mean(values), 0.0
    beta = sigma * math.sqrt(6) / math.pi
    mu = mean(values) - 0.5772 * beta
    return mu, beta


def gumbel_ppf(p: float, mu: float, beta: float) -> float:
    """Inverse CDF. p = non-exceedance prob."""
    if p <= 0 or p >= 1 or beta <= 0:
        raise ValueError
    return mu - beta * math.log(-math.log(p))


def gumbel_design(values: list[float], p_exceedance: float) -> float:
    mu, beta = gumbel_fit(values)
    return gumbel_ppf(1 - p_exceedance, mu, beta)
