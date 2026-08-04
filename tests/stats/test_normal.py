from hydrokit.stats.normal import normal_cdf, normal_ppf


def test_cdf_half():
    assert abs(normal_cdf(0) - 0.5) < 1e-6


def test_ppf():
    assert abs(normal_ppf(0.5)) < 1e-3
    assert 1.9 < normal_ppf(0.975) < 2.0
