"""CLI entry: `python -m hydrokit`."""
from __future__ import annotations

import argparse
import sys

from hydrokit import __version__


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="hydrokit")
    p.add_argument("--version", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.version:
        print(__version__)
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
