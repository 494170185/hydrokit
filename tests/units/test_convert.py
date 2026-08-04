import pytest

from hydrokit.units.convert import convert


def test_same():
    assert convert(3, "m", "m") == 3


def test_km_m():
    assert convert(1, "km", "m") == 1000


def test_unknown():
    with pytest.raises(ValueError):
        convert(1, "foo", "bar")
