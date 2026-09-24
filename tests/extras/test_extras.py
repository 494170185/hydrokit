"""Regression tests for extension modules."""
from __future__ import annotations

import datetime as dt

from hydrokit.catchment.geometry import CatchmentGeometry
from hydrokit.catchment.land_use import LandUse, composite_cn
from hydrokit.catchment.slope import mean_slope, slope_10_85
from hydrokit.catchment.streams import StreamReach, topological_order, upstream_of
from hydrokit.catchment.time_of_concentration import kandil_tc, kirpich_tc, velocity_method
from hydrokit.channel.conveyance import compound_q, conveyance
from hydrokit.channel.sections import (
    circular_area,
    rect_area,
    rect_wetted_perimeter,
    trap_area,
)
from hydrokit.core.dataclass_io import from_dict, to_dict
from hydrokit.core.math_utils import exp_decay, growth_curve, weighted_mean
from hydrokit.core.sequence import first_nonzero_index, moving_average, rolling_sum
from hydrokit.evap.source_data import MetDaily
from hydrokit.evap.thornthwaite import thornthwaite_heat_index, thornthwaite_pet
from hydrokit.infiltration.philip import PhilipModel
from hydrokit.precip.design_depth import design_depth_at, standard_durations
from hydrokit.precip.gauges import Gauge, idw
from hydrokit.precip.idf import IDFCurve
from hydrokit.precip.rain_indices import consecutive_wet_days, dry_days, wet_days
from hydrokit.precip.storm_catalog import get as storm_catalog_get
from hydrokit.reporting.design_memo import DesignMemo
from hydrokit.reporting.tables import align_table
from hydrokit.routing.storage import StorageRouter
from hydrokit.runoff.baseflow import recession_constant, straight_line
from hydrokit.runoff.hydrograph_stats import hydrograph_volume_m3, peak_and_time
from hydrokit.runoff.philip_curve import philip_effective
from hydrokit.stats.annual_series import annual_maxima, pot_series
from hydrokit.stats.log_normal import ln_design
from hydrokit.stats.ranks import percentiles, ranks
from hydrokit.stats.regression import linregress

# === stats extras ===

def test_annual_maxima():
    stamps = [dt.datetime(2024, m, 1) for m in range(1, 13)] + [dt.datetime(2025, m, 1) for m in range(1, 13)]
    vals = [float(m) for m in range(1, 13)] + [float(m) * 2 for m in range(1, 13)]
    res = annual_maxima(stamps, vals)
    assert res[0][0] == 2024 and res[0][1] == 12.0
    assert res[1][0] == 2025 and res[1][1] == 24.0


def test_pot():
    stamps = [dt.datetime(2024, 1, i + 1) for i in range(5)]
    vals = [1, 5, 3, 10, 2]
    xs = pot_series(stamps, vals, threshold=4)
    assert len(xs) == 2


def test_ln_design():
    vals = [10.0, 12.0, 15.0, 18.0, 20.0]
    v = ln_design(vals, 0.01)
    assert v > max(vals)


def test_ranks():
    r = ranks([10, 30, 20])
    # 30 → rank1, 20 → rank2, 10 → rank3
    assert r == [3, 1, 2]


def test_percentiles():
    ps = percentiles([1, 2, 3, 4, 5], [0, 50, 100])
    assert ps == [1, 3, 5]


def test_linregress():
    slope, intercept, r2 = linregress([1, 2, 3, 4], [2, 4, 6, 8])
    assert abs(slope - 2) < 1e-9
    assert abs(intercept) < 1e-9
    assert r2 > 0.99


# === precip extras ===

def test_storm_catalog():
    d = storm_catalog_get("cn_2020_10y_60min")
    assert "a" in d and "n" in d


def test_design_depth():
    c = IDFCurve(a=20.0, c=0.4, b=10.0, n=0.7)
    out = design_depth_at(c, [30, 60], 20)
    assert 30 in out and 60 in out
    assert out[60] > out[30]


def test_standard_durations():
    assert 1440 in standard_durations()


def test_gauge_idw():
    g1 = Gauge("s1", "a", 0, 0)
    g2 = Gauge("s2", "b", 1, 0)
    v = idw((0.5, 0), [g1, g2], [10.0, 20.0], power=2.0)
    assert 10.0 < v < 20.0


def test_rain_indices():
    assert consecutive_wet_days([0, 1, 2, 0, 0, 3, 4, 5]) == 3
    assert dry_days([0, 1, 0, 5], threshold=0.5) == 2
    assert wet_days([0, 1, 0, 5], threshold=0.5) == 2


# === catchment extras ===

def test_geometry():
    g = CatchmentGeometry(area_km2=50, perimeter_km=40, mainstream_length_km=18)
    assert g.compactness > 0
    assert g.form_factor > 0


def test_slopes():
    elevs = [100, 120, 150, 200, 280]
    dists = [0, 1000, 2000, 3000, 4000]
    assert slope_10_85(elevs, dists) > 0
    assert mean_slope(elevs, dists) > 0


def test_tc():
    assert kirpich_tc(5.0, 0.01) > 0
    assert kandil_tc(5.0, 1.0, 75) > 0
    assert velocity_method([(1000, 1.0), (500, 0.5)]) > 0


def test_composite_cn():
    areas = [(LandUse.FOREST, "B", 5), (LandUse.URBAN_HIGH, "B", 5)]
    cn = composite_cn(areas)
    forest = composite_cn([(LandUse.FOREST, "B", 1)])
    urban = composite_cn([(LandUse.URBAN_HIGH, "B", 1)])
    assert forest < cn < urban


def test_streams():
    reaches = {
        "c": StreamReach("c", 1, 0.001, 0.03, upstream_ids=["a", "b"]),
        "a": StreamReach("a", 1, 0.001, 0.03),
        "b": StreamReach("b", 1, 0.001, 0.03),
    }
    assert set(upstream_of("c", reaches)) == {"a", "b"}
    order = topological_order(reaches)
    assert order.index("c") > order.index("a")


# === channel extras ===

def test_sections():
    assert rect_area(5, 2) == 10
    assert rect_wetted_perimeter(5, 2) == 9
    assert trap_area(5, 2, 1.5) > rect_area(5, 2)
    assert circular_area(2, 1) > 0


def test_conveyance():
    k = conveyance(10, 1, 0.03)
    assert k > 0
    q = compound_q([(10, 1, 0.03)], 0.001)
    assert q > 0


# === routing extras ===

def test_storage_router():
    table = [(0, 0), (1000, 5), (5000, 20), (10000, 50)]
    r = StorageRouter(table, dt_hr=1.0)
    out = r.route([10, 20, 30, 20, 10])
    assert len(out) == 5


# === runoff extras ===

def test_baseflow_straight():
    flows = [1, 2, 10, 5, 2, 1]
    out = straight_line(flows, 1, 5)
    assert out[1] == 2
    assert out[4] == 2


def test_recession():
    flows = [10, 9, 8.1, 7.3, 6.6]
    k = recession_constant(flows)
    assert 0 < k < 1


def test_philip_effective():
    m = PhilipModel(sorptivity=20, conductivity=2)
    out = philip_effective([10] * 5, 1.0, m)
    assert all(x >= 0 for x in out)


def test_hydrograph_stats():
    flows = [1, 2, 3, 2, 1]
    assert hydrograph_volume_m3(flows, 60) == sum(flows) * 60
    i, v = peak_and_time(flows)
    assert v == 3 and i == 2


# === evap extras ===

def test_thornthwaite():
    monthly = [1, 3, 8, 14, 18, 22, 26, 25, 20, 14, 7, 2]
    i = thornthwaite_heat_index(monthly)
    assert i > 0
    pet = thornthwaite_pet(20, i)
    assert pet > 0


def test_met_daily():
    m = MetDaily(tmin=15, tmax=25, rs_mj_m2=20, rh_mean=60, u2_m_s=2, elevation_m=100)
    m.validate()  # no exception


# === reporting / core extras ===

def test_memo():
    d = DesignMemo("x", "y")
    d.add_section("T", "body")
    out = d.render_markdown()
    assert "x" in out and "T" in out


def test_table():
    s = align_table(["A", "B"], [["1", "2"], ["3", "4"]])
    assert "A" in s and "1" in s


def test_dataclass_io():
    from dataclasses import dataclass
    @dataclass
    class P:
        x: int
        y: str
    p = P(1, "a")
    d = to_dict(p)
    assert d == {"x": 1, "y": "a"}
    p2 = from_dict(P, d)
    assert p2 == p


def test_math_seq():
    assert weighted_mean([1, 2, 3], [1, 1, 2]) == 2.25
    assert exp_decay([1, 1, 1], 0.5)[2] < 0.5
    assert growth_curve([1, 1, 1], 0.5)[-1] < 1
    assert rolling_sum([1, 2, 3, 4], 2) == [3, 5, 7]
    assert moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
    assert first_nonzero_index([0, 0, 1, 2]) == 2
