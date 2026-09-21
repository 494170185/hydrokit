"""Build a release tarball."""
from __future__ import annotations

import tarfile
from pathlib import Path

from hydrokit import __version__


def main() -> int:
    root = Path(__file__).parent.parent
    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    name = f"hydrokit-{__version__}"
    out = dist / f"{name}.tar.gz"
    with tarfile.open(out, "w:gz") as tf:
        for pattern in ("hydrokit", "docs", "README.md", "LICENSE", "CHANGELOG.md", "pyproject.toml"):
            p = root / pattern
            if p.exists():
                tf.add(p, arcname=f"{name}/{pattern}")
    print(f"built: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
