"""Loss separation: split precip into (initial, continuing, excess)."""
from __future__ import annotations


def phi_index(precip_series_mm: list[float], step_hr: float, total_runoff_mm: float) -> float:
    """Compute φ index: constant loss rate that leaves total_runoff as excess.

    Returns mm/hr.
    """
    if not precip_series_mm or total_runoff_mm < 0:
        return 0.0
    total_p = sum(precip_series_mm)
    if total_p <= total_runoff_mm:
        return total_p / (len(precip_series_mm) * step_hr)

    # bisect on φ in [0, max_intensity]
    def excess_at(phi: float) -> float:
        return sum(max(0.0, p - phi * step_hr) for p in precip_series_mm)

    lo, hi = 0.0, max(precip_series_mm) / step_hr + 1
    for _ in range(60):
        mid = (lo + hi) / 2
        if excess_at(mid) > total_runoff_mm:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
