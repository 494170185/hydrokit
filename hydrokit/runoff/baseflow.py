"""Baseflow separation."""
from __future__ import annotations


def straight_line(flows: list[float], n_peak: int, n_end: int) -> list[float]:
    """Straight-line between pre-peak and post-storm minima."""
    if not flows or n_peak >= n_end or n_end > len(flows):
        raise ValueError
    out = [0.0] * len(flows)
    q1, q2 = flows[n_peak], flows[n_end - 1]
    for i in range(n_peak, n_end):
        t = (i - n_peak) / max(1, n_end - 1 - n_peak)
        out[i] = q1 * (1 - t) + q2 * t
    return out


def recession_constant(flows: list[float]) -> float:
    """Estimate k such that Q_t = Q_0 * k^t (log-linear fit on recession limbs)."""
    # collect recession segments: where flows[i+1] < flows[i]
    xs: list[int] = []
    ys: list[float] = []
    for i in range(len(flows) - 1):
        if flows[i + 1] < flows[i] and flows[i] > 0:
            xs.append(i)
            import math
            ys.append(math.log(flows[i]))
    if len(xs) < 2:
        return 0.95
    # least squares
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    slope = num / den if den else -0.05
    import math
    return math.exp(slope)
