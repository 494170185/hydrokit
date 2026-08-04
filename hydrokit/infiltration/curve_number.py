"""SCS Curve Number for runoff depth.

Q = (P - Ia)^2 / (P - Ia + S)  if P > Ia else 0
S = 25400 / CN - 254  (mm)
Ia = lambda * S, lambda = 0.2 (default) or 0.05
"""
from __future__ import annotations


def s_potential(cn: float) -> float:
    """Potential maximum retention (mm)."""
    if cn <= 0 or cn > 100:
        raise ValueError("CN in (0, 100]")
    return 25400.0 / cn - 254.0


def initial_abstraction(cn: float, lambda_coef: float = 0.2) -> float:
    return lambda_coef * s_potential(cn)


def runoff_depth_cn(precip_mm: float, cn: float, lambda_coef: float = 0.2) -> float:
    """Runoff depth (mm) for given precipitation and CN."""
    if precip_mm <= 0:
        return 0.0
    s = s_potential(cn)
    ia = lambda_coef * s
    if precip_mm <= ia:
        return 0.0
    return (precip_mm - ia) ** 2 / (precip_mm - ia + s)
