from hydrokit.units.area import km2_to_m2, mu_to_m2
from hydrokit.units.length import km_to_m, mm_to_m


def test_length():
    assert km_to_m(1.5) == 1500
    assert abs(mm_to_m(25) - 0.025) < 1e-12


def test_area():
    assert km2_to_m2(1) == 1e6
    assert abs(mu_to_m2(1) - 666.6666666666666) < 1e-6
