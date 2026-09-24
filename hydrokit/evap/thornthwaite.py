"""Thornthwaite monthly PET."""
from __future__ import annotations


def thornthwaite_heat_index(monthly_tmean: list[float]) -> float:
    """Sum of (T/5)^1.514 over 12 months."""
    return sum((max(t, 0) / 5) ** 1.514 for t in monthly_tmean)


def thornthwaite_pet(tmean_month: float, i_heat: float, daylight_hr_factor: float = 1.0) -> float:
    """Monthly PET (mm). i_heat from `thornthwaite_heat_index`."""
    if tmean_month <= 0:
        return 0.0
    a = 6.75e-7 * i_heat ** 3 - 7.71e-5 * i_heat ** 2 + 1.792e-2 * i_heat + 0.49239
    return 16 * daylight_hr_factor * (10 * tmean_month / max(i_heat, 1e-6)) ** a
