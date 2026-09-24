"""Conveyance and compound channel helpers."""
from __future__ import annotations

import math


def conveyance(area_m2: float, r_m: float, n: float) -> float:
    """K = (1/n) A R^(2/3)."""
    if n <= 0:
        raise ValueError
    return (1.0 / n) * area_m2 * (r_m ** (2 / 3))


def compound_q(panels: list[tuple[float, float, float]], s0: float) -> float:
    """Q over compound section. panels = [(area, r, n)]."""
    return sum(conveyance(a, r, n) * math.sqrt(s0) for a, r, n in panels)
