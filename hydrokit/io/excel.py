"""Excel-like wide table reader (TSV / space-delimited)."""
from __future__ import annotations

from pathlib import Path


def read_table(path: str | Path, sep: str = "\t") -> list[dict[str, str]]:
    """Read a simple table file with header. sep = tab or space."""
    rows: list[dict[str, str]] = []
    with Path(path).open("r", encoding="utf-8") as fh:
        lines = [ln.rstrip("\n") for ln in fh]
    if not lines:
        return []
    header = lines[0].split(sep)
    for line in lines[1:]:
        if not line.strip():
            continue
        cells = line.split(sep)
        rows.append(dict(zip(header, cells)))
    return rows
