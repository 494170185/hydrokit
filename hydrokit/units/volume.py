"""Volume conversions."""


def mm_per_km2_to_m3(depth_mm: float, area_km2: float) -> float:
    """Convert area-averaged depth to volume."""
    return depth_mm / 1000.0 * area_km2 * 1e6


def m3_to_mm_per_km2(volume_m3: float, area_km2: float) -> float:
    """Inverse."""
    if area_km2 == 0:
        return 0.0
    return volume_m3 / (area_km2 * 1e6) * 1000.0
