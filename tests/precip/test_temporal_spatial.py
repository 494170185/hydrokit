from hydrokit.precip.areal_reduction import arf_logarithmic
from hydrokit.precip.spatial import areal_mean, area_reduction_factor, thiessen_weights
from hydrokit.precip.temporal import scs_type_ii, triangular_pattern, uniform_pattern


def test_uniform():
    assert sum(uniform_pattern(60, 6)) == 60


def test_triangular():
    p = triangular_pattern(60, 6)
    assert abs(sum(p) - 60) < 1e-6


def test_scs():
    p = scs_type_ii(24)
    assert abs(sum(p) - 1.0) < 1e-9


def test_arf():
    assert area_reduction_factor(0) == 1.0
    assert 0.3 < area_reduction_factor(100) < 1.0


def test_thiessen():
    ws = thiessen_weights([1, 1, 2])
    assert abs(sum(ws) - 1) < 1e-9
    assert ws[2] == 0.5


def test_areal():
    v = areal_mean([10.0, 20.0, 30.0], thiessen_weights([1, 1, 2]))
    assert v == 22.5


def test_arf_log():
    assert arf_logarithmic(0) == 1.0
    assert arf_logarithmic(100) < 1.0
