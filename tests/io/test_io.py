import datetime as dt

from hydrokit.io.csv import read_series, write_series
from hydrokit.io.excel import read_table
from hydrokit.io.json import read_json, write_json
from hydrokit.io.resample import resample_sum, resample_uniform
from hydrokit.io.timeseries import TimeSeries


def test_csv_roundtrip(tmp_path):
    p = tmp_path / "ts.csv"
    write_series(p, [("t1", 1.0), ("t2", 2.0)])
    out = read_series(p)
    assert out == [("t1", 1.0), ("t2", 2.0)]


def test_json_roundtrip(tmp_path):
    p = tmp_path / "obj.json"
    write_json(p, {"a": 1, "b": [1, 2]})
    assert read_json(p)["a"] == 1


def test_table_read(tmp_path):
    p = tmp_path / "t.tsv"
    p.write_text("name\tvalue\na\t1\nb\t2\n", encoding="utf-8")
    rows = read_table(p)
    assert len(rows) == 2 and rows[0]["name"] == "a"


def test_timeseries_basic():
    s = TimeSeries(
        stamps=[dt.datetime(2026, 1, 1, h) for h in range(4)],
        values=[1.0, 2.0, 3.0, 4.0],
    )
    assert len(s) == 4
    assert s.max() == 4.0
    assert s.mean() == 2.5


def test_timeseries_clip():
    s = TimeSeries(
        stamps=[dt.datetime(2026, 1, 1, h) for h in range(6)],
        values=[float(h) for h in range(6)],
    )
    c = s.clip(dt.datetime(2026, 1, 1, 1), dt.datetime(2026, 1, 1, 3))
    assert len(c) == 3
    assert c.values == [1.0, 2.0, 3.0]


def test_resample_uniform():
    stamps = [dt.datetime(2026, 1, 1, 0, m, 0) for m in range(4)]
    values = [0.0, 1.0, 2.0, 3.0]
    out_s, out_v = resample_uniform(stamps, values, step_s=30)
    assert len(out_s) > len(stamps)


def test_resample_sum():
    stamps = [dt.datetime(2026, 1, 1, 0, 0, s) for s in range(10)]
    values = [1.0] * 10
    out_s, out_v = resample_sum(stamps, values, new_step_s=3)
    total = sum(out_v)
    assert total == 10.0
