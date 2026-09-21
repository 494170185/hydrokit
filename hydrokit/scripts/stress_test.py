"""Performance sanity for common workloads."""
from __future__ import annotations

import time

from hydrokit.precip.design_storm import chicago_hyetograph
from hydrokit.precip.idf import IDFCurve
from hydrokit.routing.muskingum import MuskingumRouter


def main() -> int:
    curve = IDFCurve(a=20, c=0.4, b=10, n=0.7)
    t0 = time.monotonic()
    for _ in range(200):
        chicago_hyetograph(curve, 360, 5, 20)
    print(f"chicago_storm x200: {time.monotonic() - t0:.3f}s")

    r = MuskingumRouter(k_hr=3.0, x=0.2, dt_hr=0.5)
    inflow = [10.0 + i * 0.1 for i in range(2000)]
    t0 = time.monotonic()
    for _ in range(50):
        r.route(inflow)
    print(f"muskingum x50 (2000 pts): {time.monotonic() - t0:.3f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
