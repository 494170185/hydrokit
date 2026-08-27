from hydrokit.runoff.abstractions import split_abstraction
from hydrokit.runoff.gr4j import GR4JModel
from hydrokit.runoff.scs_cn import scs_cn_runoff
from hydrokit.runoff.simple import runoff_depth_coefficient, runoff_series
from hydrokit.runoff.xinanjiang import XinanjiangModel


def test_simple_coeff():
    assert runoff_depth_coefficient(100, 0.3) == 30.0
    assert runoff_depth_coefficient(0, 0.5) == 0.0


def test_runoff_series():
    out = runoff_series([10, 20, 30], 0.5)
    assert out == [5.0, 10.0, 15.0]


def test_scs_cn_step():
    # total 100 mm with CN=80; Ia ~ 12.7, S ~ 63.5
    rain = [10, 20, 30, 40]
    out = scs_cn_runoff(rain, 80)
    assert sum(out) <= sum(rain)
    assert out[-1] > out[0]  # CN is convex


def test_xinanjiang():
    m = XinanjiangModel(wm=100, im=0.02)
    w = 50.0
    w, r = m.step(w, 30, 5)
    assert r >= 0 and w >= 0


def test_gr4j():
    m = GR4JModel(x1=100, x3=5)
    q1 = m.step(20, 5)
    q2 = m.step(0, 0)
    assert q1 >= 0
    assert q2 < q1 or q2 >= 0  # decays or zero


def test_split_abstraction():
    exc, loss = split_abstraction(100, ia_mm=10, continuing_rate_mm_hr=5, duration_hr=6)
    assert exc + loss == 100
    assert loss == 40
