"""Rainfall indices: annual max, daily max, wet/dry days."""
from __future__ import annotations


def consecutive_wet_days(values: list[float], threshold: float = 0.1) -> int:
    """Longest streak of values >= threshold."""
    best = cur = 0
    for v in values:
        if v >= threshold:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def dry_days(values: list[float], threshold: float = 0.1) -> int:
    return sum(1 for v in values if v < threshold)


def wet_days(values: list[float], threshold: float = 0.1) -> int:
    return sum(1 for v in values if v >= threshold)


def intensity_hist(values: list[float], bins: list[float]) -> list[int]:
    """Count values into [b0, b1), [b1, b2), ..., [b_{n-1}, inf)."""
    out = [0] * len(bins)
    for v in values:
        for i, b in enumerate(bins):
            upper = bins[i + 1] if i + 1 < len(bins) else float("inf")
            if b <= v < upper:
                out[i] += 1
                break
    return out
