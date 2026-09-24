"""Standard storm event catalog for regression testing."""
from __future__ import annotations

CATALOG: dict[str, dict] = {
    "cn_2020_10y_60min": {
        "a": 22.0, "c": 0.42, "b": 12.0, "n": 0.72,
        "description": "华南典型",
    },
    "cn_2020_50y_120min": {
        "a": 24.0, "c": 0.50, "b": 15.0, "n": 0.75,
        "description": "华南大暴雨",
    },
    "cn_north_20y_30min": {
        "a": 18.0, "c": 0.38, "b": 8.0, "n": 0.68,
        "description": "华北典型",
    },
}


def get(name: str) -> dict:
    if name not in CATALOG:
        raise KeyError(f"storm catalog not found: {name}")
    return CATALOG[name]


def list_names() -> list[str]:
    return list(CATALOG.keys())
