"""Unified convertor."""
from __future__ import annotations

from hydrokit.units import area as A
from hydrokit.units import flow as F
from hydrokit.units import length as L
from hydrokit.units import time as T

_MAP = {
    ("km", "m"): L.km_to_m, ("m", "km"): L.m_to_km,
    ("mm", "m"): L.mm_to_m, ("m", "mm"): L.m_to_mm,
    ("cm", "m"): L.cm_to_m, ("m", "cm"): L.m_to_cm,
    ("km2", "m2"): A.km2_to_m2, ("m2", "km2"): A.m2_to_km2,
    ("ha", "m2"): A.ha_to_m2, ("m2", "ha"): A.m2_to_ha,
    ("mu", "m2"): A.mu_to_m2, ("m2", "mu"): A.m2_to_mu,
    ("hr", "s"): T.hr_to_s, ("s", "hr"): T.s_to_hr,
    ("min", "s"): T.min_to_s, ("s", "min"): T.s_to_min,
    ("day", "s"): T.day_to_s, ("s", "day"): T.s_to_day,
    ("m3/s", "m3/h"): F.m3s_to_m3h, ("m3/h", "m3/s"): F.m3h_to_m3s,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    fn = _MAP.get((from_unit, to_unit))
    if fn is None:
        raise ValueError(f"no conversion {from_unit!r} -> {to_unit!r}")
    return fn(value)
