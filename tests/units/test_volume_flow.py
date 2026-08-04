from hydrokit.units.flow import m3s_to_mmhr, mmhr_to_m3s
from hydrokit.units.volume import m3_to_mm_per_km2, mm_per_km2_to_m3


def test_volume():
    v = mm_per_km2_to_m3(10, 5)
    assert v == 10 * 1e-3 * 5 * 1e6
    d = m3_to_mm_per_km2(v, 5)
    assert abs(d - 10) < 1e-6


def test_flow():
    assert abs(mmhr_to_m3s(10, 5) - 10 / 3600 * 5e6 / 1000) < 1e-6
    back = m3s_to_mmhr(mmhr_to_m3s(10, 5), 5)
    assert abs(back - 10) < 1e-6
