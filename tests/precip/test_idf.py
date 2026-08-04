from hydrokit.precip.idf import IDFCurve


def test_intensity_decreases_with_duration():
    c = IDFCurve(a=20.0, c=0.4, b=10.0, n=0.7)
    i60 = c.intensity(60, 20)
    i30 = c.intensity(30, 20)
    assert i30 > i60


def test_total():
    c = IDFCurve(a=20.0, c=0.4, b=10.0, n=0.7)
    d = c.total_depth(60, 20)
    assert d > 0
