"""Smoke tests for the CLI."""
from __future__ import annotations

from hydrokit.cli.main import main


def test_version(capsys):
    rc = main(["--version"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "1.0.2" in out


def test_storm(capsys):
    rc = main(["storm", "--duration", "60", "--step", "5", "--T", "20"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "total" in out


def test_runoff(capsys):
    rc = main(["runoff", "--p", "100", "--cn", "80"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "runoff depth" in out
