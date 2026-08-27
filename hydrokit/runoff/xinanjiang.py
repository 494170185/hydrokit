"""新安江 (Xinanjiang) saturation-excess runoff model (single-layer)."""
from __future__ import annotations


class XinanjiangModel:
    """Simple XAJ with tension water storage and runoff yield at saturation.

    Parameters:
      wm: tension water capacity (mm) typically 80-200
      im: impervious area fraction (0-0.05 typical)
    """

    def __init__(self, wm: float = 120.0, im: float = 0.02) -> None:
        if wm <= 0:
            raise ValueError("wm must be positive")
        if not 0 <= im < 1:
            raise ValueError("im in [0, 1)")
        self.wm = wm
        self.im = im

    def step(self, state_w: float, precip: float, evap: float) -> tuple[float, float]:
        """One timestep.

        Returns (new_w, runoff_mm). state_w = tension water (mm).
        """
        w = state_w + precip
        # saturation → runoff
        if w > self.wm:
            runoff = (w - self.wm) * (1 - self.im) + self.im * precip
            w = self.wm
        else:
            runoff = self.im * precip
        # evap: simple proportional
        e = min(evap, w)
        w -= e
        return max(0.0, w), max(0.0, runoff)
