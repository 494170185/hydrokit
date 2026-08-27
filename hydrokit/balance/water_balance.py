"""Simple water balance: P - ET - Q - ΔS = 0 (with residuals)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Balance:
    precip: float
    et: float
    runoff: float
    delta_storage: float

    @property
    def residual(self) -> float:
        return self.precip - self.et - self.runoff - self.delta_storage

    def close(self, tol: float = 1e-3) -> bool:
        return abs(self.residual) <= tol
