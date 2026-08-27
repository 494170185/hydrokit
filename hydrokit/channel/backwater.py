"""Gradually varied flow: standard step method for backwater curves."""
from __future__ import annotations

import math

G = 9.81


class GVFProfile:
    """Compute depth profile y(x) upstream of a control section."""

    def __init__(self, b_m: float, s0: float, n: float) -> None:
        self.b = b_m
        self.s0 = s0
        self.n = n

    def _energy(self, y: float, v: float) -> float:
        return y + v * v / (2 * G)

    def _friction_slope(self, v: float, r: float) -> float:
        # Manning: Sf = n² v² / R^(4/3)
        return self.n ** 2 * v ** 2 / (r ** (4 / 3))

    def step(self, x_ds: float, y_ds: float, dx: float, q: float, n_steps: int) -> list[tuple[float, float]]:
        """Integrate upstream by dx each step. Returns [(x, y)] upstream."""
        out: list[tuple[float, float]] = [(x_ds, y_ds)]
        y = y_ds
        x = x_ds
        for _ in range(n_steps):
            area = self.b * y
            v = q / area
            r = area / (self.b + 2 * y)
            e1 = self._energy(y, v)
            sf = self._friction_slope(v, r)
            dx_eff = -abs(dx)
            de_dx = self.s0 - sf
            e2 = e1 + de_dx * dx_eff
            # solve y2 from e2 = y2 + v2²/(2g); bisect
            lo, hi = 0.01, max(2.0, 2 * y)
            for _ in range(40):
                mid = (lo + hi) / 2
                a2 = self.b * mid
                v2 = q / a2
                e_mid = self._energy(mid, v2)
                if e_mid < e2:
                    lo = mid
                else:
                    hi = mid
            y = (lo + hi) / 2
            x += dx_eff
            out.append((x, y))
        return out
