"""Convolution: apply UH to excess rainfall series."""
from __future__ import annotations


def convolve(excess_mm: list[float], uh_ordinates: list[float]) -> list[float]:
    """Return direct runoff hydrograph. Units preserved.

    excess_mm[i] * uh_ords[j] summed into output[i+j].
    """
    if not excess_mm or not uh_ordinates:
        return []
    n = len(excess_mm) + len(uh_ordinates) - 1
    out = [0.0] * n
    for i, exc in enumerate(excess_mm):
        if exc == 0:
            continue
        for j, uh in enumerate(uh_ordinates):
            out[i + j] += exc * uh
    return out


def s_curve_from_uh(uh_ords: list[float], repetitions: int = 10) -> list[float]:
    """Build S-curve by summing UH shifted by its own duration."""
    if not uh_ordinates or repetitions <= 0:
        return []
    out = [0.0] * (len(uh_ords) + repetitions)
    for r in range(repetitions):
        for i, q in enumerate(uh_ords):
            out[r + i] += q
    return out
