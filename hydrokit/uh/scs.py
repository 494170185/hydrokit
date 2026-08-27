"""SCS (NRCS) dimensionless unit hydrograph."""
from __future__ import annotations

import math

# SCS dimensionless UH ratios (t/tp, q/qp) — standard tabulation
_SCS_DUH = [
    (0.0, 0.000), (0.1, 0.030), (0.2, 0.100), (0.3, 0.190), (0.4, 0.310),
    (0.5, 0.470), (0.6, 0.660), (0.7, 0.820), (0.8, 0.930), (0.9, 0.990),
    (1.0, 1.000), (1.1, 0.990), (1.2, 0.930), (1.3, 0.860), (1.4, 0.780),
    (1.5, 0.680), (1.6, 0.560), (1.7, 0.460), (1.8, 0.390), (1.9, 0.330),
    (2.0, 0.280), (2.2, 0.207), (2.4, 0.147), (2.6, 0.107), (2.8, 0.077),
    (3.0, 0.055), (3.2, 0.040), (3.4, 0.029), (3.6, 0.021), (3.8, 0.015),
    (4.0, 0.011), (4.5, 0.005), (5.0, 0.000),
]


def scs_peak_flow(runoff_mm: float, area_km2: float, tp_hr: float) -> float:
    """Peak discharge q_p (m^3/s) for SCS UH: q_p = 0.208 * A * Q / tp."""
    if tp_hr <= 0:
        raise ValueError("tp must be positive")
    return 0.208 * area_km2 * runoff_mm / tp_hr


def scs_tp_from_tc(tc_hr: float, duration_hr: float) -> float:
    """Time to peak: tp = 0.6 * tc + 0.5 * D (SCS relationship)."""
    return 0.6 * tc_hr + 0.5 * duration_hr


def scs_lag_time(tc_hr: float) -> float:
    """SCS lag: L = 0.6 * tc."""
    return 0.6 * tc_hr


def scs_uh(area_km2: float, tc_hr: float, duration_hr: float, runoff_mm: float = 1.0, step_hr: float = 0.1) -> tuple[list[float], list[float]]:
    """Generate SCS UH: (times_hr, q in m^3/s per mm)."""
    tp = scs_tp_from_tc(tc_hr, duration_hr)
    qp = scs_peak_flow(runoff_mm, area_km2, tp)
    n = max(10, int(5.0 * tp / step_hr))
    times: list[float] = []
    qs: list[float] = []
    for i in range(n + 1):
        t = i * step_hr
        ratio = t / tp
        # interpolate
        if ratio >= 5.0:
            q = 0.0
        else:
            q = _interp_ratio(ratio, _SCS_DUH) * qp
        times.append(t)
        qs.append(q)
    return times, qs


def _interp_ratio(r: float, table: list[tuple[float, float]]) -> float:
    if r <= table[0][0]:
        return table[0][1]
    if r >= table[-1][0]:
        return table[-1][1]
    for i in range(len(table) - 1):
        a, b = table[i], table[i + 1]
        if a[0] <= r <= b[0]:
            t = (r - a[0]) / (b[0] - a[0]) if b[0] != a[0] else 0.5
            return a[1] * (1 - t) + b[1] * t
    return 0.0


def s_curve(uh_times: list[float], uh_ords: list[float], step_hr: float) -> list[float]:
    """S-curve: sum UH ordinates shifted by step duration."""
    n = len(uh_ords)
    out = [0.0] * (n + 20)
    for offset in range(20):
        for i, q in enumerate(uh_ords):
            out[offset + i] += q
    # normalize by step: S-curve approaches 1/step * UH area asymptote
    return out
