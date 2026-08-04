from hydrokit.stats.p3 import design_value, kp_from_p


def test_kp_cs0():
    assert abs(kp_from_p(0.0, 0.01) - 2.33) < 0.1


def test_design_value_gt_max():
    xs = [100.0, 120.0, 140.0, 160.0, 180.0]
    v = design_value(xs, p=0.01, cs_ratio=3.5)
    assert v > max(xs)
