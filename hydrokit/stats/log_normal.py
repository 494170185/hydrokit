"""Log-normal distribution helpers."""
from __future__ import annotations

import math

from hydrokit.stats.normal import normal_ppf


def ln_ppf(p: float, mean_log: float, sd_log: float) -> float:
    return math.exp(normal_ppf(p, mean_log, sd_log))


def ln_fit(values: list[float]) -> tuple[float, float]:
    """Method of moments on log-transform."""
    logs = [math.log(v) for v in values if v > 0]
    if not logs:
        raise ValueError("no positive values")
    m = sum(logs) / len(logs)
    s2 = sum((x - m) ** 2 for x in logs) / (len(logs) - 1) if len(logs) > 1 else 0.0
    return m, math.sqrt(s2)


def ln_design(values: list[float], p_exceedance: float) -> float:
    m, s = ln_fit(values)
    return ln_ppf(1 - p_exceedance, m, s)
