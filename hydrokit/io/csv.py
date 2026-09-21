"""CSV I/O."""
from __future__ import annotations

import csv
from pathlib import Path


def read_series(path: str | Path, time_col: str = "time", value_col: str = "value") -> list[tuple[str, float]]:
    """Read two-column CSV (header required)."""
    out: list[tuple[str, float]] = []
    with Path(path).open("r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            out.append((row[time_col], float(row[value_col])))
    return out


def write_series(path: str | Path, rows: list[tuple[str, float]], header: tuple[str, str] = ("time", "value")) -> Path:
    """Write two-column CSV."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        writer.writerows(rows)
    return path
