from hydrokit.core.utils import clamp, interpolate, safe_div, trapezoid


def test_clamp():
    assert clamp(5, 0, 3) == 3
    assert clamp(-1, 0, 3) == 0


def test_safe_div():
    assert safe_div(1, 0) == 0
    assert safe_div(4, 2) == 2


def test_trapezoid():
    xs = [0, 1, 2]
    ys = [0, 1, 0]
    assert trapezoid(xs, ys) == 1.0


def test_interpolate():
    assert interpolate(0.5, [0, 1], [0, 10]) == 5
    assert interpolate(2, [0, 1], [0, 10]) == 10
