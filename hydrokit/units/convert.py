"""Unified convertor."""
from __future__ import annotations

from hydrokit.units import area as area_u
from hydrokit.units import flow as flow_u
from hydrokit.units import length as length_u
from hydrokit.units import time as time_u

_MAP = {
    ("km", "m"): length_u.km_to_m, ("m", "km"): length_u.m_to_km,
    ("mm", "m"): length_u.mm_to_m, ("m", "mm"): length_u.m_to_mm,
    ("cm", "m"): length_u.cm_to_m, ("m", "cm"): length_u.m_to_cm,
    ("km2", "m2"): area_u.km2_to_m2, ("m2", "km2"): area_u.m2_to_km2,
    ("ha", "m2"): area_u.ha_to_m2, ("m2", "ha"): area_u.m2_to_ha,
    ("mu", "m2"): area_u.mu_to_m2, ("m2", "mu"): area_u.m2_to_mu,
    ("hr", "s"): time_u.hr_to_s, ("s", "hr"): time_u.s_to_hr,
    ("min", "s"): time_u.min_to_s, ("s", "min"): time_u.s_to_min,
    ("day", "s"): time_u.day_to_s, ("s", "day"): time_u.s_to_day,
    ("m3/s", "m3/h"): flow_u.m3s_to_m3h, ("m3/h", "m3/s"): flow_u.m3h_to_m3s,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    fn = _MAP.get((from_unit, to_unit))
    if fn is None:
        raise ValueError(f"no conversion {from_unit!r} -> {to_unit!r}")
    return fn(value)
