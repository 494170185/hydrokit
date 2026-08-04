from hydrokit.infiltration.curve_number import (
    initial_abstraction,
    runoff_depth_cn,
    s_potential,
)
from hydrokit.infiltration.green_ampt import GreenAmptModel
from hydrokit.infiltration.horton import HortonModel, effective_rainfall_horton
from hydrokit.infiltration.philip import PhilipModel
from hydrokit.infiltration.soil_moisture import AMC, adjust_cn_for_amc


def test_horton_rate_decreasing():
    m = HortonModel(f0=50, fc=5, k=2.0)
    assert m.rate(0) == 50
    assert m.rate(1) < 50
    assert m.rate(10) < m.rate(5)


def test_horton_cumulative():
    m = HortonModel(f0=50, fc=5, k=2.0)
    assert m.cumulative(1) > 0
    assert m.cumulative(10) > m.cumulative(5)


def test_horton_effective():
    m = HortonModel(f0=20, fc=5, k=2.0)
    rain = [10.0] * 6
    excess = effective_rainfall_horton(rain, 1.0, m)
    assert all(e >= 0 for e in excess)
    assert sum(excess) < sum(rain)


def test_philip():
    m = PhilipModel(sorptivity=20.0, conductivity=2.0)
    assert m.cumulative(1) > 0
    assert m.rate(1) > m.rate(4)


def test_green_ampt():
    m = GreenAmptModel(k=5.0, psi=200.0, delta_theta=0.3)
    assert m.rate(0) == float("inf")
    assert m.rate(100) > 0
    tp = m.time_to_ponding(50.0)
    assert 0 < tp < 10


def test_cn():
    s = s_potential(80)
    assert s > 0
    ia = initial_abstraction(80)
    assert ia > 0
    q = runoff_depth_cn(100, 80)
    assert 0 < q < 100


def test_cn_edge():
    assert runoff_depth_cn(0, 80) == 0.0
    assert runoff_depth_cn(1, 80) == 0.0  # below Ia


def test_amc():
    cn_ii = 75.0
    assert adjust_cn_for_amc(cn_ii, AMC.AVERAGE) == cn_ii
    assert adjust_cn_for_amc(cn_ii, AMC.DRY) < cn_ii
    assert adjust_cn_for_amc(cn_ii, AMC.WET) > cn_ii
