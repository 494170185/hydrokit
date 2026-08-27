from hydrokit.balance.abstractions import phi_index
from hydrokit.balance.bucket import Bucket
from hydrokit.balance.water_balance import Balance


def test_balance_closure():
    b = Balance(precip=100, et=40, runoff=50, delta_storage=10)
    assert b.close()


def test_balance_residual():
    b = Balance(precip=100, et=40, runoff=30, delta_storage=10)
    assert abs(b.residual - 20) < 1e-9


def test_bucket():
    bk = Bucket(capacity_mm=100, initial_mm=50, drainage_rate=0.1)
    r, e, s = bk.step(precip=30, et=10)
    assert r >= 0 and e >= 0 and 0 <= s <= 100


def test_bucket_overflow():
    bk = Bucket(capacity_mm=50, initial_mm=45)
    r, _, _ = bk.step(precip=20, et=0)
    assert r >= 15  # overflow + drainage


def test_phi_index():
    p = [10, 20, 30, 10]
    phi = phi_index(p, step_hr=1.0, total_runoff_mm=20)
    assert phi > 0
    # excess with this phi should ≈ 20
    excess = sum(max(0, x - phi) for x in p)
    assert abs(excess - 20) < 2
