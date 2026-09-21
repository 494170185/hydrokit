"""Resample & interpolate time series."""
from __future__ import annotations

import datetime as dt

from hydrokit.core.utils import interpolate


def resample_uniform(
    stamps: list[dt.datetime], values: list[float], step_s: int,
) -> tuple[list[dt.datetime], list[float]]:
    """Linear interpolate to uniform step."""
    if not stamps:
        return [], []
    t0, t_end = stamps[0], stamps[-1]
    xs = [s.timestamp() for s in stamps]
    out_stamps: list[dt.datetime] = []
    out_values: list[float] = []
    t = t0
    while t <= t_end:
        out_stamps.append(t)
        out_values.append(interpolate(t.timestamp(), xs, values))
        t += dt.timedelta(seconds=step_s)
    return out_stamps, out_values


def resample_sum(
    stamps: list[dt.datetime], values: list[float], new_step_s: int,
) -> tuple[list[dt.datetime], list[float]]:
    """Aggregate by sum (for precipitation / flows)."""
    if not stamps:
        return [], []
    out_stamps: list[dt.datetime] = []
    out_values: list[float] = []
    bucket_start = stamps[0]
    bucket: list[float] = []
    for s, v in zip(stamps, values):
        if (s - bucket_start).total_seconds() >= new_step_s:
            out_stamps.append(bucket_start)
            out_values.append(sum(bucket))
            bucket_start = s
            bucket = [v]
        else:
            bucket.append(v)
    if bucket:
        out_stamps.append(bucket_start)
        out_values.append(sum(bucket))
    return out_stamps, out_values
