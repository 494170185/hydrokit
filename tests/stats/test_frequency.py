from hydrokit.stats.frequency import cs, cv, plotting_positions_weibull, std


def test_pp():
    xs = [1.0, 2.0, 3.0]
    pp = plotting_positions_weibull(xs)
    assert pp[0][0] == 3.0
    assert abs(pp[0][1] - 25.0) < 1e-9


def test_std_cv():
    xs = [1.0, 2.0, 3.0]
    assert abs(std(xs) - 1.0) < 1e-6
    assert abs(cv(xs) - 0.5) < 1e-6


def test_cs():
    xs = [1.0, 2.0, 3.0, 4.0, 50.0]
    assert cs(xs) > 1
