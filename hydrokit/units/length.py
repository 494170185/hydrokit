"""Length conversions (SI canonical = meter)."""


def km_to_m(v: float) -> float: return v * 1000.0
def m_to_km(v: float) -> float: return v / 1000.0
def mm_to_m(v: float) -> float: return v / 1000.0
def m_to_mm(v: float) -> float: return v * 1000.0
def cm_to_m(v: float) -> float: return v / 100.0
def m_to_cm(v: float) -> float: return v * 100.0
