from hydrokit.stats.gumbel import gumbel_design, gumbel_fit


def test_fit():
    xs = [10.0, 12.0, 15.0, 18.0, 20.0]
    mu, beta = gumbel_fit(xs)
    assert beta > 0
    assert mu < max(xs)


def test_design():
    xs = [10.0, 12.0, 15.0, 18.0, 20.0]
    v50 = gumbel_design(xs, 0.5)
    v01 = gumbel_design(xs, 0.01)
    assert v01 > v50
