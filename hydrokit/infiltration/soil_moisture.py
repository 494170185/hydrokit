"""Antecedent soil moisture accounting (AMC I/II/III)."""
from __future__ import annotations

from enum import Enum


class AMC(str, Enum):
    DRY = "I"      # AMC I: dry
    AVERAGE = "II" # AMC II: average
    WET = "III"    # AMC III: wet


def adjust_cn_for_amc(cn_ii: float, amc: AMC) -> float:
    """Convert AMC-II CN to AMC-I (dry) or AMC-III (wet)."""
    if amc == AMC.AVERAGE:
        return cn_ii
    if amc == AMC.DRY:
        return cn_ii / (2.281 - 0.01281 * cn_ii)
    if amc == AMC.WET:
        return cn_ii / (0.427 + 0.00573 * cn_ii)
    raise ValueError(amc)
