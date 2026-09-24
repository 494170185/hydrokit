"""Design memo writer."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DesignMemo:
    project: str
    author: str
    sections: list[tuple[str, str]] = field(default_factory=list)

    def add_section(self, title: str, body: str) -> DesignMemo:
        self.sections.append((title, body))
        return self

    def render_markdown(self) -> str:
        lines = [f"# {self.project} 设计备忘", f"作者：{self.author}", ""]
        for title, body in self.sections:
            lines.append(f"## {title}")
            lines.append("")
            lines.append(body)
            lines.append("")
        return "\n".join(lines)
