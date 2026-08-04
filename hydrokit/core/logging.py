"""Logging setup."""
from __future__ import annotations

import logging
import sys

_configured = False


def configure(level: str = "INFO") -> None:
    global _configured
    root = logging.getLogger("hydrokit")
    root.setLevel(level)
    if not root.handlers:
        ch = logging.StreamHandler(sys.stderr)
        ch.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
        root.addHandler(ch)
    _configured = True


def get_logger(name: str) -> logging.Logger:
    if not _configured:
        configure()
    return logging.getLogger(f"hydrokit.{name}")
