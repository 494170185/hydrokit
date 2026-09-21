"""Snyder synthetic UH (regional)."""
from __future__ import annotations


def snyder_lag(l_main_km: float, l_centroid_km: float, ct: float = 2.0) -> float:
    """Basin lag in hours. ct typical 1.8-2.2 (mountain smaller)."""
    return ct * (l_main_km * l_centroid_km) ** 0.3


def snyder_peak(area_km2: float, lag_hr: float, cp: float = 0.6) -> float:
    """Peak discharge per unit rainfall depth (m^3/s per mm). cp typical 0.5-0.7."""
    if lag_hr <= 0:
        raise ValueError
    return cp * area_km2 / lag_hr


def snyder_uh(area_km2: float, l_main_km: float, l_centroid_km: float, duration_hr: float, step_hr: float = 0.25,
              ct: float = 2.0, cp: float = 0.6) -> tuple[list[float], list[float]]:
    """Generate Snyder UH (triangle), normalized to exactly 1 mm of runoff depth."""
    lag = snyder_lag(l_main_km, l_centroid_km, ct)
    tp = lag + duration_hr / 2
    qp = snyder_peak(area_km2, lag, cp)
    tb = 5.0 * tp
    n = max(10, int(tb / step_hr))
    times: list[float] = []
    qs: list[float] = []
    for i in range(n + 1):
        t = i * step_hr
        if t < tp:
            q = qp * t / tp
        elif t < tb:
            q = qp * (tb - t) / (tb - tp)
        else:
            q = 0.0
        times.append(t)
        qs.append(q)
    # normalize so the hydrograph volume = 1 mm over the basin area
    vol = sum(q * step_hr for q in qs) * 3600.0  # m^3
    target = 1e-3 * area_km2 * 1e6  # 1 mm depth in m^3
    if vol > 0:
        factor = target / vol
        qs = [q * factor for q in qs]
    return times, qs
