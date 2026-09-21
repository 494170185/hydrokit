"""Timeseries container."""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass


@dataclass
class TimeSeries:
    stamps: list[dt.datetime]
    values: list[float]

    def __post_init__(self) -> None:
        if len(self.stamps) != len(self.values):
            raise ValueError("stamps and values length mismatch")

    def __len__(self) -> int:
        return len(self.values)

    def max(self) -> float:
        return max(self.values) if self.values else 0.0

    def sum(self) -> float:
        return sum(self.values)

    def mean(self) -> float:
        return sum(self.values) / len(self.values) if self.values else 0.0

    def clip(self, start: dt.datetime, end: dt.datetime) -> TimeSeries:
        pairs = [(s, v) for s, v in zip(self.stamps, self.values) if start <= s <= end]
        return TimeSeries([p[0] for p in pairs], [p[1] for p in pairs])
