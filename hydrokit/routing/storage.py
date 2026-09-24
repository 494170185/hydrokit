"""Storage / level-pool reservoir routing."""
from __future__ import annotations


class StorageRouter:
    """Puls method: S₂ - S₁ = (I₁+I₂)/2 Δt - (O₁+O₂)/2 Δt."""

    def __init__(self, storage_outflow_table: list[tuple[float, float]], dt_hr: float) -> None:
        """storage_outflow_table: [(S_m3, O_m3s)] monotonically increasing."""
        if dt_hr <= 0:
            raise ValueError
        self.table = sorted(storage_outflow_table)
        self.dt_s = dt_hr * 3600.0
        self._s_vals = [s for s, _ in self.table]
        self._o_vals = [o for _, o in self.table]

    def _interp(self, s: float, from_table: list[float], to_table: list[float]) -> float:
        if s <= from_table[0]:
            return to_table[0]
        if s >= from_table[-1]:
            return to_table[-1]
        for i in range(len(from_table) - 1):
            a, b = from_table[i], from_table[i + 1]
            if a <= s <= b:
                t = (s - a) / (b - a) if b != a else 0.5
                return to_table[i] * (1 - t) + to_table[i + 1] * t
        return to_table[-1]

    def route(self, inflow: list[float], o_init: float = 0.0) -> list[float]:
        if not inflow:
            return []
        s = self._s_vals[0] + o_init * self.dt_s
        out: list[float] = [o_init]
        for i in range(1, len(inflow)):
            i_avg = (inflow[i - 1] + inflow[i]) / 2
            # solve for s_new from continuity with new outflow
            # iterate (simple fixed point)
            o_guess = out[-1]
            for _ in range(20):
                o_avg = (out[-1] + o_guess) / 2
                s_new = s + (i_avg - o_avg) * self.dt_s
                o_guess = self._interp(s_new, self._s_vals, self._o_vals)
            out.append(o_guess)
            s = s_new
        return out
