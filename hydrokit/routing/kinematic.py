"""Kinematic wave routing (1D simple form)."""
from __future__ import annotations


class KinematicWaveRouter:
    """q_next = (q_prev * dt + q_local * dx) / (dt / c + dt) with wave celerity c."""

    def __init__(self, celerity_m_s: float, dx_m: float, dt_s: float) -> None:
        if celerity_m_s <= 0 or dx_m <= 0 or dt_s <= 0:
            raise ValueError
        self.c = celerity_m_s
        self.dx = dx_m
        self.dt = dt_s

    def route(self, inflow_upstream: list[float], inflow_local: list[float] | None = None) -> list[float]:
        """Route upstream hydrograph down one reach, adding local inflow."""
        if not inflow_upstream:
            return []
        local = inflow_local or [0.0] * len(inflow_upstream)
        if len(local) != len(inflow_upstream):
            raise ValueError("local inflow length mismatch")
        courant = self.c * self.dt / self.dx
        out: list[float] = [inflow_upstream[0] + local[0]]
        for i in range(1, len(inflow_upstream)):
            q = (1 - courant) * out[-1] + courant * inflow_upstream[i - 1] + local[i]
            out.append(max(0.0, q))
        return out
