from hydrokit.precip.design_storm import chicago_hyetograph
from hydrokit.precip.idf import IDFCurve


def test_hyetograph_volume():
    curve = IDFCurve(a=20.0, c=0.4, b=10.0, n=0.7)
    total = curve.total_depth(60, 20)
    hs = chicago_hyetograph(curve, 60, 5, 20)
    assert abs(sum(hs) - total) / total < 0.05


def test_peak_in_middle():
    curve = IDFCurve(a=20.0, c=0.4, b=10.0, n=0.7)
    hs = chicago_hyetograph(curve, 60, 5, 20, peak_coeff=0.42)
    peak_idx = max(range(len(hs)), key=lambda i: hs[i])
    # peak_coeff=0.42 → tp = 25.2min, step 5min → peak idx ≈ 4-5 (of 12)
    assert 3 <= peak_idx <= 6
