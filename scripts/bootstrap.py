"""Bootstrap dev environment."""
from __future__ import annotations

import subprocess
import sys


def main() -> int:
    subprocess.call([sys.executable, "-m", "pip", "install", "-e", "."])
    subprocess.call([sys.executable, "-m", "pip", "install", "pytest", "ruff"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
