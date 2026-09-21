"""Run tests + lint + secret scan."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][A-Za-z0-9_/-]{12,}['\"]"),
    re.compile(r"-----BEGIN (RSA|OPENSSH|PGP) PRIVATE KEY-----"),
]


def scan_secrets(root: Path) -> list[str]:
    findings: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in (".py", ".md", ".txt", ".yml", ".yaml", ".json", ".toml"):
            continue
        if any(p.startswith(".") or p in ("node_modules", "dist", ".venv", "__pycache__") for p in path.parts):
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(content.splitlines(), start=1):
            for pat in SECRET_PATTERNS:
                if pat.search(line):
                    findings.append(f"{path.relative_to(root)}:{i}: {line[:100]}")
    return findings


def main() -> int:
    root = Path(__file__).parent.parent
    rc = 0
    rc |= subprocess.call([sys.executable, "-m", "pytest", "-q"], cwd=root)
    rc |= subprocess.call([sys.executable, "-m", "ruff", "check", "hydrokit", "tests"], cwd=root)
    f = scan_secrets(root)
    if f:
        for x in f:
            print("SECRET?:", x)
        rc = 1
    else:
        print("secrets: clean")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
