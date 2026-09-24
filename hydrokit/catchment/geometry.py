"""Catchment geometry: area, perimeter, shape factors."""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class CatchmentGeometry:
    area_km2: float
    perimeter_km: float
    mainstream_length_km: float
    centroid_distance_km: float = 0.0
    mean_elevation_m: float = 0.0

    @property
    def compactness(self) -> float:
        """Gravelius index Kc = P / (2 √(π A))."""
        if self.area_km2 <= 0:
            return 0.0
        return self.perimeter_km / (2 * math.sqrt(math.pi * self.area_km2))

    @property
    def elongation_ratio(self) -> float:
        """Re = 2 √(A / π) / L_main."""
        if self.mainstream_length_km <= 0:
            return 0.0
        return 2 * math.sqrt(self.area_km2 / math.pi) / self.mainstream_length_km

    @property
    def form_factor(self) -> float:
        """FF = A / L² (shape factor)."""
        if self.mainstream_length_km <= 0:
            return 0.0
        return self.area_km2 / self.mainstream_length_km ** 2
