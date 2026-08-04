"""Time conversions (SI = s)."""


def hr_to_s(v: float) -> float: return v * 3600.0
def s_to_hr(v: float) -> float: return v / 3600.0
def min_to_s(v: float) -> float: return v * 60.0
def s_to_min(v: float) -> float: return v / 60.0
def day_to_s(v: float) -> float: return v * 86400.0
def s_to_day(v: float) -> float: return v / 86400.0
