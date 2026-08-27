import math

from hydrokit.channel.backwater import GVFProfile
from hydrokit.channel.critical_depth import critical_depth_rectangular, critical_depth_trapezoid
from hydrokit.channel.hydraulic_jump import conjugate_depth_rectangular, energy_loss_jump
from hydrokit.channel.manning import (
    hydraulic_radius_rectangular,
    hydraulic_radius_trapezoid,
    manning_q,
)
from hydrokit.channel.normal_depth import normal_depth_trapezoid


def test_manning_q():
    # Wide channel: A = 10*1 = 10, R ≈ 1 (deep relative to wide)
    q = manning_q(r_m=1.0, s0=0.001, n=0.03, area_m2=10.0)
    expected = (1 / 0.03) * 10 * 1 * math.sqrt(0.001)
    assert abs(q - expected) < 1e-6


def test_hydraulic_radius_rect():
    r = hydraulic_radius_rectangular(10, 1)
    assert abs(r - 10 / 12) < 1e-6


def test_hydraulic_radius_trap():
    r = hydraulic_radius_trapezoid(5, 2, 1.5)
    assert r > 0


def test_normal_depth_rect_ish():
    # approximates rectangular when z=0
    q_target = 5.0
    y = normal_depth_trapezoid(q_m3s=q_target, n=0.03, s0=0.0005, b_m=10.0, side_slope=0.0)
    # verify by feeding back
    a = 10.0 * y
    r = a / (10.0 + 2 * y)
    q_back = manning_q(r, 0.0005, 0.03, a)
    assert abs(q_back - q_target) / q_target < 0.01


def test_critical_depth():
    yc = critical_depth_rectangular(q_m3s=10.0, width_m=5.0)
    # yc = (100 / (9.81 * 25))^(1/3) ≈ 0.742
    assert abs(yc - 0.742) < 0.01


def test_critical_trap():
    yc = critical_depth_trapezoid(q_m3s=10.0, b_m=5, side_slope=1.0)
    assert 0 < yc < 5


def test_jump():
    y2 = conjugate_depth_rectangular(y1=0.5, v1=6.0)
    assert y2 > 0.5
    loss = energy_loss_jump(0.5, y2)
    assert loss > 0


def test_gvf():
    p = GVFProfile(b_m=10, s0=0.0005, n=0.03)
    profile = p.step(x_ds=1000, y_ds=1.5, dx=-100, q=10.0, n_steps=5)
    assert len(profile) == 6
    assert profile[0][0] == 1000
    # dx=-100 repeated 5 times → x decreases by 500 → last x = 500
    assert profile[-1][0] == 500
