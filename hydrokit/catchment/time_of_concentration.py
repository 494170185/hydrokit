"""Time of concentration estimators."""
from __future__ import annotations


def kirpich_tc(length_km: float, slope: float) -> float:
    """Kirpich (USDA, rural): tc (hr) = 0.01947 * L^0.77 * S^-0.385 (L in m, S in m/m)."""
    if length_km <= 0 or slope <= 0:
        raise ValueError
    return 0.01947 * (length_km * 1000) ** 0.77 * slope ** -0.385 / 60.0


def kandil_tc(length_km: float, slope: float, cn: float) -> float:
    """SCS Lag equation: tc = L^0.8 * (1000/CN - 9)^0.7 / (1900 * S^0.5) (L in km, S in %)."""
    if length_km <= 0 or slope <= 0 or cn <= 0 or cn >= 100:
        raise ValueError
    return (length_km * 1000) ** 0.8 * (1000 / cn - 9) ** 0.7 / (1900 * slope ** 0.5)


def velocity_method(segments: list[tuple[float, float]]) -> float:
    """tc = Σ L_i / V_i. segments = [(length_m, velocity_m_s)]."""
    return sum(L / max(v, 1e-6) for L, v in segments) / 3600.0
