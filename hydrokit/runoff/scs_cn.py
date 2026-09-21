"""SCS-CN event runoff model + step-by-step version."""
from __future__ import annotations

from hydrokit.infiltration.curve_number import s_potential


def scs_cn_runoff(precip_series: list[float], cn: float, lambda_coef: float = 0.2) -> list[float]:
    """Apply CN model step-by-step: each step's P accumulates, runoff increments."""
    s = s_potential(cn)
    ia = lambda_coef * s
    p_cum = 0.0
    q_prev = 0.0
    out: list[float] = []
    for p in precip_series:
        p_cum += p
        q_cum = ((p_cum - ia) ** 2 / (p_cum - ia + s)) if p_cum > ia else 0.0
        out.append(q_cum - q_prev)
        q_prev = q_cum
    return out
