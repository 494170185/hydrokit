"""Muskingum-Cunge routing."""
from __future__ import annotations


def cunge_params(dt_hr: float, dx_m: float, celerity_m_s: float, diffusivity: float) -> tuple[float, float]:
    """Estimate K and X from hydraulic parameters.

    K = dx / celerity (s) converted to hr.
    X from diffusivity matching: x = 0.5 * (1 - q_ref / (B * s0 * c * dx))
    Simplified: X = 0.5 * (1 - diffusivity * 2 / (celerity * dx_m))
    """
    k_hr = (dx_m / max(1e-6, celerity_m_s)) / 3600.0
    x = 0.5 * (1 - 2 * diffusivity / (celerity_m_s * dx_m))
    x = max(0.0, min(0.5, x))
    return k_hr, x


class MuskingumCungeRouter:
    """Same recurrence as Muskingum; parameters derived from hydraulics."""

    def __init__(self, k_hr: float, x: float, dt_hr: float) -> None:
        from hydrokit.routing.muskingum import MuskingumRouter
        self._router = MuskingumRouter(k_hr, x, dt_hr)

    def route(self, inflow: list[float]) -> list[float]:
        return self._router.route(inflow)
