"""Simplified GR4J conceptual model (2 stores)."""
from __future__ import annotations

import math


class GR4JModel:
    """Minimal GR4J: production store (x1) + routing store (x2), x3 = UH1 time base.

    Only the production/routing store accounting is implemented; the two UHs
    of the full GR4J are collapsed into a single linear reservoir for clarity.
    """

    def __init__(self, x1: float = 100.0, x2: float = 0.0, x3: float = 20.0) -> None:
        self.x1 = max(1.0, x1)
        self.x2 = x2
        self.x3 = max(0.5, x3)
        self.s = 0.0   # production store mm
        self.r = 0.0   # routing store mm

    def _production(self, p: float, e: float) -> tuple[float, float]:
        """Return (net rain, actual evap)."""
        if p >= e:
            pn = p - e
            en = 0.0
        else:
            pn = 0.0
            en = e - p
            # reduce store by en
            if self.s <= en:
                en = self.s
                self.s = 0.0
            else:
                self.s -= en
        # percolation from production store
        if self.s > 0:
            perc = self.s * (1 - (1 + (4 * self.s / (9 * self.x1)) ** 4) ** (-0.25))
        else:
            perc = 0.0
        self.s += pn - perc
        self.s = max(0.0, min(self.x1, self.s))
        return pn + perc, en

    def step(self, precip: float, evap: float) -> float:
        net, _ = self._production(precip, evap)
        # routing store with exponential depletion
        self.r += net
        outflow = self.r * (1 - math.exp(-1.0 / self.x3))
        self.r -= outflow
        return max(0.0, outflow)
