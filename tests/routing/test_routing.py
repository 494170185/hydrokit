from hydrokit.routing.kinematic import KinematicWaveRouter
from hydrokit.routing.lag import attenuate, lag
from hydrokit.routing.muskingum import MuskingumRouter
from hydrokit.routing.muskingum_cunge import MuskingumCungeRouter, cunge_params


def test_muskingum_inertia():
    r = MuskingumRouter(k_hr=3.0, x=0.2, dt_hr=1.0)
    inflow = [10, 20, 30, 25, 15, 5]
    out = r.route(inflow)
    assert len(out) == len(inflow)
    # peak attenuated
    assert max(out) <= max(inflow) + 5
    # phase lag: peak delayed
    assert out.index(max(out)) >= inflow.index(max(inflow))


def test_muskingum_mass():
    r = MuskingumRouter(k_hr=2.0, x=0.2, dt_hr=0.5)
    inflow = [10, 10, 10, 10, 10, 10]
    out = r.route(inflow)
    assert abs(sum(out) - sum(inflow)) / sum(inflow) < 0.2


def test_cunge():
    k, x = cunge_params(dt_hr=0.5, dx_m=1000, celerity_m_s=2.0, diffusivity=100)
    assert k > 0 and 0 <= x <= 0.5
    r = MuskingumCungeRouter(k, x, dt_hr=0.5)
    out = r.route([10] * 10)
    assert len(out) == 10


def test_lag():
    out = lag([1, 2, 3], 2)
    assert out == [0, 0, 1, 2, 3]


def test_attenuate():
    out = attenuate([100, 0, 0], alpha=0.5)
    assert out[0] == 100
    assert out[1] == 50


def test_kinematic():
    r = KinematicWaveRouter(celerity_m_s=2.0, dx_m=500, dt_s=60)
    out = r.route([10] * 5)
    assert len(out) == 5
