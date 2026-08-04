"""Area conversions (SI = m^2)."""


def km2_to_m2(v: float) -> float: return v * 1e6
def m2_to_km2(v: float) -> float: return v / 1e6
def ha_to_m2(v: float) -> float: return v * 1e4
def m2_to_ha(v: float) -> float: return v / 1e4


def mu_to_m2(v: float) -> float: return v * 2000.0 / 3.0  # 1 亩 = 666.67 m²
def m2_to_mu(v: float) -> float: return v * 3.0 / 2000.0
