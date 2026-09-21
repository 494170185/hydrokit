"""Normal depth via bisection on Manning's equation."""
from __future__ import annotations

from hydrokit.channel.manning import hydraulic_radius_trapezoid, manning_q


def _q_trapezoid(y: float, b: float, z: float) -> tuple[float, float]:
    """(area, hydraulic radius) for trapezoid."""
    area = (b + z * y) * y
    r = hydraulic_radius_trapezoid(b, y, z)
    return area, r


def normal_depth_trapezoid(
    q_m3s: float, n: float, s0: float, b_m: float, side_slope: float,
    tol: float = 1e-4, max_iter: int = 80,
) -> float:
    """Solve Q = 1/n * A * R^(2/3) sqrt(S0) for depth via bisection."""
    if q_m3s <= 0 or n <= 0 or s0 <= 0 or b_m <= 0:
        raise ValueError

    def q_of(y: float) -> float:
        area, r = _q_trapezoid(y, b_m, side_slope)
        return manning_q(r, s0, n, area)

    # expand upper bound
    hi = 0.1
    for _ in range(20):
        if q_of(hi) >= q_m3s:
            break
        hi *= 2.0
    lo = 0.0
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        if q_of(mid) < q_m3s:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2
