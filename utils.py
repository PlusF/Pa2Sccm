from constants import *


def calculate_volume_cylinder(diameter_mm: float, length_m: float) -> float:
    return PI * (diameter_mm * 1e-3) ** 2 / 4 * length_m


def calculate_mol_from_PVT(pressure_Pa: float, volume_m3: float, temperature_celsius: float) -> float:
    return pressure_Pa * volume_m3 / (R * (temperature_celsius + T_0))


def calculate_sccm(n_mol: float, time_min: float) -> float:
    return V_std_m3 * 1e6 * n_mol / time_min
