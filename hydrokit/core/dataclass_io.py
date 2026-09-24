"""Dataclass serialization."""
from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any, TypeVar

T = TypeVar("T")


def to_dict(obj: Any) -> dict:
    if is_dataclass(obj) and not isinstance(obj, type):
        return asdict(obj)
    return dict(obj)


def from_dict(cls: type[T], data: dict) -> T:
    return cls(**data)
