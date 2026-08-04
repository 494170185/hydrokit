"""Time helpers."""
from __future__ import annotations

import datetime as dt


def parse(s: str) -> dt.datetime:
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return dt.datetime.fromisoformat(s)


def add_hours(d: dt.datetime, h: float) -> dt.datetime:
    return d + dt.timedelta(hours=h)


def hours_between(a: dt.datetime, b: dt.datetime) -> float:
    return (b - a).total_seconds() / 3600.0
