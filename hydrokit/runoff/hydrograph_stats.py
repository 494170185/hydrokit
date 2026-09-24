"""Hydrograph statistics."""
from __future__ import annotations


def hydrograph_volume_m3(flows_m3s: list[float], step_s: float) -> float:
    return sum(flows_m3s) * step_s


def peak_and_time(flows: list[float]) -> tuple[int, float]:
    if not flows:
        return 0, 0.0
    i = max(range(len(flows)), key=lambda k: flows[k])
    return i, flows[i]


def baseflow_index(flows: list[float], baseflow_estimate: float) -> float:
    mean_flow = sum(flows) / len(flows) if flows else 0.0
    if mean_flow == 0:
        return 0.0
    return baseflow_estimate / mean_flow
