"""Initial & continuing abstraction split."""
from __future__ import annotations


def split_abstraction(precip_mm: float, ia_mm: float, continuing_rate_mm_hr: float, duration_hr: float) -> tuple[float, float]:
    """Split precip into runoff excess vs total loss.

    Returns (excess_mm, loss_mm).
    """
    if precip_mm <= 0:
        return 0.0, 0.0
    ia_used = min(ia_mm, precip_mm)
    rest = precip_mm - ia_used
    cont_loss = min(continuing_rate_mm_hr * duration_hr, rest)
    excess = rest - cont_loss
    loss = ia_used + cont_loss
    return max(0.0, excess), max(0.0, loss)
