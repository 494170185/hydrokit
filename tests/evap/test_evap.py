from hydrokit.evap.hargreaves import extraterrestrial_radiation, hargreaves
from hydrokit.evap.pan import pan_to_et0, pan_to_lake_evaporation
from hydrokit.evap.penman import (
    penman_monteith_daily,
    psychrometric_constant,
    saturation_vapor_pressure_kpa,
    slope_vapor_pressure_curve,
)
from hydrokit.evap.priestley_taylor import priestley_taylor


def test_sat_vp():
    es = saturation_vapor_pressure_kpa(20)
    # ≈ 2.338 kPa
    assert 2.30 < es < 2.40


def test_slope_vp():
    d = slope_vapor_pressure_curve(20)
    assert d > 0


def test_gamma():
    g = psychrometric_constant(0)
    assert 0.05 < g < 0.08


def test_pm_et0():
    et = penman_monteith_daily(
        tmin=15.0, tmax=25.0,
        rs_mj_m2=20.0, rh_mean=60.0, u2_m_s=2.0, elevation_m=100,
    )
    assert 1 < et < 10


def test_pt():
    et = priestley_taylor(t_mean=20.0, rn_mj_m2=15.0, elevation_m=100)
    assert et > 0


def test_hargreaves_ra():
    ra = extraterrestrial_radiation(lat_deg=30, day_of_year=180)
    assert ra > 20


def test_hargreaves():
    et = hargreaves(tmean=20, tmin=15, tmax=28, lat_deg=30, day_of_year=180)
    assert et > 0


def test_pan():
    assert pan_to_lake_evaporation(5) == 5 * 0.7
    assert pan_to_et0(5) == 5 * 0.85
