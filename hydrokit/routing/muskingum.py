"""Muskingum flood routing.

O_2 = C0 * I_2 + C1 * I_1 + C2 * O_1
Storage: S = K * (x I + (1-x) O)
"""
from __future__ import annotations


class MuskingumRouter:
    def __init__(self, k_hr: float, x: float, dt_hr: float) -> None:
        if k_hr <= 0:
            raise ValueError("k must be positive")
        if not 0 <= x <= 0.5:
            raise ValueError("x in [0, 0.5]")
        if dt_hr <= 0:
            raise ValueError("dt must be positive")
        self.k = k_hr
        self.x = x
        self.dt = dt_hr
        # coefficients
        denom = k_hr - k_hr * x + 0.5 * dt_hr
        if denom <= 0:
            raise ValueError(f"unstable: dt={dt_hr} too large vs k={k_hr}")
        self.c0 = (0.5 * dt_hr - k_hr * x) / denom
        self.c1 = (0.5 * dt_hr + k_hr * x) / denom
        self.c2 = (k_hr - k_hr * x - 0.5 * dt_hr) / denom

    def route(self, inflow: list[float]) -> list[float]:
        """Route inflow series → outflow series (same length)."""
        if not inflow:
            return []
        out: list[float] = [inflow[0]]
        for i in range(1, len(inflow)):
            o_next = self.c0 * inflow[i] + self.c1 * inflow[i - 1] + self.c2 * out[i - 1]
            out.append(max(0.0, o_next))
        return out
