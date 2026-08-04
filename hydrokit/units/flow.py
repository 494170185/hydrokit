"""Flow conversions."""


def m3s_to_m3h(v: float) -> float: return v * 3600.0
def m3h_to_m3s(v: float) -> float: return v / 3600.0


def mmhr_to_m3s(rate_mm_hr: float, area_km2: float) -> float:
    """Areal rainfall intensity -> runoff m^3/s."""
    return rate_mm_hr / 1000.0 * area_km2 * 1e6 / 3600.0


def m3s_to_mmhr(flow_m3s: float, area_km2: float) -> float:
    """Inverse."""
    if area_km2 == 0:
        return 0.0
    return flow_m3s * 3600.0 * 1000.0 / (area_km2 * 1e6)
