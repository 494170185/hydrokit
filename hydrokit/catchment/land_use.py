"""Land use categories + composite CN."""
from __future__ import annotations

from enum import Enum


class LandUse(str, Enum):
    FOREST = "forest"
    PASTURE = "pasture"
    CROPLAND = "cropland"
    URBAN_LOW = "urban_low"
    URBAN_HIGH = "urban_high"
    WATER = "water"
    WETLAND = "wetland"


# CN values for AMC-II (typical from TR-55)
CN_TABLE: dict[LandUse, dict[str, int]] = {
    LandUse.FOREST: {"A": 30, "B": 55, "C": 70, "D": 77},
    LandUse.PASTURE: {"A": 39, "B": 61, "C": 74, "D": 80},
    LandUse.CROPLAND: {"A": 67, "B": 78, "C": 85, "D": 89},
    LandUse.URBAN_LOW: {"A": 57, "B": 72, "C": 81, "D": 86},
    LandUse.URBAN_HIGH: {"A": 89, "B": 92, "C": 94, "D": 95},
    LandUse.WATER: {"A": 100, "B": 100, "C": 100, "D": 100},
    LandUse.WETLAND: {"A": 85, "B": 85, "C": 85, "D": 85},
}


def composite_cn(areas: list[tuple[LandUse, str, float]]) -> float:
    """Weighted composite CN. areas = [(land_use, soil_group, area_km2)]."""
    if not areas:
        raise ValueError
    total = sum(a for _, _, a in areas)
    if total <= 0:
        raise ValueError
    s = 0.0
    for lu, sg, a in areas:
        s += CN_TABLE[lu][sg] * a
    return s / total
