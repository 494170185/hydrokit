"""Rank & ordering utilities."""
from __future__ import annotations


def ranks(values: list[float], descending: bool = True) -> list[int]:
    """1-based rank of each value. Ties assigned average."""
    indexed = list(enumerate(values))
    indexed.sort(key=lambda kv: kv[1], reverse=descending)
    r = [0] * len(values)
    i = 0
    while i < len(indexed):
        j = i
        while j + 1 < len(indexed) and indexed[j + 1][1] == indexed[i][1]:
            j += 1
        avg_rank = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[indexed[k][0]] = avg_rank
        i = j + 1
    return r


def percentiles(values: list[float], ps: list[float]) -> list[float]:
    """Compute percentile values at p ∈ [0, 100]."""
    if not values:
        return [0.0] * len(ps)
    s = sorted(values)
    out: list[float] = []
    for p in ps:
        k = p / 100 * (len(s) - 1)
        lo = int(k)
        hi = min(len(s) - 1, lo + 1)
        t = k - lo
        out.append(s[lo] * (1 - t) + s[hi] * t)
    return out
