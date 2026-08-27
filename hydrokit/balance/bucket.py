"""Linear reservoir (bucket) soil water model."""
from __future__ import annotations


class Bucket:
    """Single-store soil moisture bucket."""

    def __init__(self, capacity_mm: float, initial_mm: float = 0.0, drainage_rate: float = 0.1) -> None:
        if capacity_mm <= 0:
            raise ValueError
        self.cap = capacity_mm
        self.storage = max(0.0, min(capacity_mm, initial_mm))
        self.k = drainage_rate  # per step

    def step(self, precip: float, et: float) -> tuple[float, float, float]:
        """Return (runoff_mm, actual_et_mm, storage_after_mm)."""
        # precipitation adds
        self.storage += precip
        runoff = max(0.0, self.storage - self.cap)
        self.storage = min(self.cap, self.storage)
        # ET: limited by storage
        actual_et = min(et, self.storage)
        self.storage -= actual_et
        # drainage as runoff
        drain = self.k * self.storage
        self.storage -= drain
        return runoff + drain, actual_et, self.storage
