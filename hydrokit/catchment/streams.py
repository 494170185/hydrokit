"""Stream network metadata."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class StreamReach:
    id: str
    length_km: float
    slope: float
    n_manning: float
    upstream_ids: list[str] = field(default_factory=list)


def upstream_of(reach_id: str, reaches: dict[str, StreamReach]) -> list[str]:
    """Recursive upstream reach IDs."""
    out: list[str] = []
    stack = list(reaches[reach_id].upstream_ids)
    seen: set[str] = set()
    while stack:
        r = stack.pop()
        if r in seen or r not in reaches:
            continue
        seen.add(r)
        out.append(r)
        stack.extend(reaches[r].upstream_ids)
    return out


def topological_order(reaches: dict[str, StreamReach]) -> list[str]:
    """Return reach IDs in upstream → downstream order."""
    visited: dict[str, str] = {}
    out: list[str] = []

    def visit(rid: str) -> None:
        state = visited.get(rid)
        if state == "done":
            return
        if state == "in_progress":
            raise ValueError("cycle detected")
        visited[rid] = "in_progress"
        if rid in reaches:
            for up in reaches[rid].upstream_ids:
                visit(up)
        visited[rid] = "done"
        out.append(rid)

    for rid in reaches:
        visit(rid)
    return out
