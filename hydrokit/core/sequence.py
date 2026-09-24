"""Sequence utilities."""
from __future__ import annotations


def rolling_sum(values: list[float], window: int) -> list[float]:
    out: list[float] = []
    for i in range(len(values) - window + 1):
        out.append(sum(values[i : i + window]))
    return out


def rolling_max(values: list[float], window: int) -> list[float]:
    return [max(values[i : i + window]) for i in range(len(values) - window + 1)]


def rolling_min(values: list[float], window: int) -> list[float]:
    return [min(values[i : i + window]) for i in range(len(values) - window + 1)]


def moving_average(values: list[float], window: int) -> list[float]:
    return [sum(values[i : i + window]) / window for i in range(len(values) - window + 1)]


def first_nonzero_index(values: list[float]) -> int:
    for i, v in enumerate(values):
        if v != 0:
            return i
    return -1


def last_nonzero_index(values: list[float]) -> int:
    for i in range(len(values) - 1, -1, -1):
        if values[i] != 0:
            return i
    return -1
