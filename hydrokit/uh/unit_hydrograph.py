"""Unit hydrograph representation & basic algebra."""
from __future__ import annotations

from dataclasses import dataclass

from hydrokit.core.utils import trapezoid


@dataclass
class UnitHydrograph:
    """Discrete UH: flows per unit of excess rainfall depth."""
    times: list[float]     # hr
    ordinates: list[float]  # m^3/s per mm of excess (or arbitrary units)

    def __post_init__(self) -> None:
        if len(self.times) != len(self.ordinates):
            raise ValueError("times and ordinates must have same length")

    @property
    def duration_hr(self) -> float:
        return self.times[-1] - self.times[0] if self.times else 0.0

    def volume_m3_per_mm(self) -> float:
        """Area under UH = volume per unit depth of excess."""
        return trapezoid(self.times, self.ordinates) * 3600.0

    def peak(self) -> tuple[float, float]:
        """(time of peak, peak value)."""
        if not self.ordinates:
            return 0.0, 0.0
        i = max(range(len(self.ordinates)), key=lambda k: self.ordinates[k])
        return self.times[i], self.ordinates[i]

    def scale(self, factor: float) -> UnitHydrograph:
        return UnitHydrograph(list(self.times), [q * factor for q in self.ordinates])
