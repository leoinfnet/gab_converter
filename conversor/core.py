from __future__ import annotations


# -------- Temperatura --------
def celsius_para_fahrenheit(c: float) -> float:
    return c * 9.0 / 5.0 + 32.0


def fahrenheit_para_celsius(f: float) -> float:
    return (f - 32.0) * 5.0 / 9.0


def celsius_para_kelvin(c: float) -> float:
    return c + 273.15


def kelvin_para_celsius(k: float) -> float:
    return k - 273.15


# -------- Distância --------
_KM_POR_MILHA = 1.609344


def km_para_milhas(km: float) -> float:
    return km / _KM_POR_MILHA


def milhas_para_km(mi: float) -> float:
    return mi * _KM_POR_MILHA


# -------- Peso --------
_LB_POR_KG = 2.2046226218487757  # valor preciso


def kg_para_lb(kg: float) -> float:
    return kg * _LB_POR_KG


def lb_para_kg(lb: float) -> float:
    return lb / _LB_POR_KG
