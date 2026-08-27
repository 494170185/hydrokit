from hydrokit.uh.clark import clark_iuh
from hydrokit.uh.convolution import convolve
from hydrokit.uh.scs import scs_peak_flow, scs_tp_from_tc, scs_uh
from hydrokit.uh.snyder import snyder_lag, snyder_peak, snyder_uh
from hydrokit.uh.unit_hydrograph import UnitHydrograph


def test_scs_peak():
    q = scs_peak_flow(runoff_mm=10, area_km2=20, tp_hr=2.0)
    assert q > 0
    assert q / (10 * 20 / 2) > 0.15  # around 0.208 factor


def test_scs_tp():
    tp = scs_tp_from_tc(tc_hr=3.0, duration_hr=1.0)
    assert tp > 0


def test_scs_uh_shape():
    ts, qs = scs_uh(area_km2=10, tc_hr=3, duration_hr=1, runoff_mm=1.0, step_hr=0.2)
    assert len(ts) == len(qs)
    assert max(qs) > 0
    assert qs[0] == 0.0
    # peak ≈ tp
    pk_idx = max(range(len(qs)), key=lambda i: qs[i])
    tp = scs_tp_from_tc(3, 1)
    assert abs(ts[pk_idx] - tp) < 0.6


def test_snyder():
    lag = snyder_lag(15.0, 8.0)
    qp = snyder_peak(100, lag)
    assert lag > 0 and qp > 0


def test_snyder_uh():
    ts, qs = snyder_uh(area_km2=100, l_main_km=15, l_centroid_km=8, duration_hr=1.0)
    assert max(qs) > 0
    # volume ≈ 1 mm over 100 km² = 100,000 m^3 (exact due to normalization)
    from hydrokit.core.utils import trapezoid
    v = trapezoid(ts, qs) * 3600
    expected = 1e-3 * 100e6
    assert abs(v - expected) / expected < 0.01


def test_clark():
    ts, qs = clark_iuh(tc_hr=0.5, r_hr=2.0, step_hr=0.1)
    assert max(qs) > 0
    assert len(ts) == len(qs)


def test_convolve_simple():
    uh = [0.5, 0.5]
    excess = [1.0]
    out = convolve(excess, uh)
    assert out == [0.5, 0.5]


def test_convolve_two_pulses():
    uh = [1.0, 0.0]
    excess = [1.0, 2.0, 0.5]
    out = convolve(excess, uh)
    # length = 3 + 2 - 1 = 4; uh[1]=0 so tail is 0
    assert out[0] == 1.0
    assert out[1] == 2.0
    assert out[2] == 0.5
    assert len(out) == 4


def test_uh_dataclass():
    uh = UnitHydrograph(times=[0, 1, 2], ordinates=[0, 1, 0])
    assert uh.duration_hr == 2
    tp, qp = uh.peak()
    assert tp == 1 and qp == 1
    scaled = uh.scale(2.0)
    assert scaled.ordinates == [0, 2, 0]
