"""Annual maximum / minimum series helpers."""
from __future__ import annotations

import datetime as dt


def annual_maxima(stamps: list[dt.datetime], values: list[float]) -> list[tuple[int, float]]:
    """Block maxima by calendar year."""
    if len(stamps) != len(values):
        raise ValueError
    by_year: dict[int, float] = {}
    for s, v in zip(stamps, values):
        by_year[s.year] = max(by_year.get(s.year, float("-inf")), v)
    return sorted(by_year.items())


def annual_minima(stamps: list[dt.datetime], values: list[float]) -> list[tuple[int, float]]:
    if len(stamps) != len(values):
        raise ValueError
    by_year: dict[int, float] = {}
    for s, v in zip(stamps, values):
        by_year[s.year] = min(by_year.get(s.year, float("inf")), v)
    return sorted(by_year.items())


def pot_series(stamps: list[dt.datetime], values: list[float], threshold: float) -> list[tuple[dt.datetime, float]]:
    """Peaks-over-threshold series."""
    return [(s, v) for s, v in zip(stamps, values) if v > threshold]
