from __future__ import annotations
import math
from conversor import core


def approx(a: float, b: float, tol: float = 1e-9) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


# ---- Temperatura
def test_celsius_fahrenheit_ida_volta():
    for c in (-40.0, 0.0, 37.0, 100.0):
        f = core.celsius_para_fahrenheit(c)
        c2 = core.fahrenheit_para_celsius(f)
        assert approx(c, c2, 1e-12)


def test_celsius_kelvin_basico():
    assert approx(core.celsius_para_kelvin(0.0), 273.15)
    assert approx(core.kelvin_para_celsius(273.15), 0.0)


# ---- Distância
def test_km_milhas_ida_volta():
    for km in (0.0, 1.0, 5.3, 42.195):
        mi = core.km_para_milhas(km)
        km2 = core.milhas_para_km(mi)
        assert approx(km, km2)


# ---- Peso
def test_kg_lb_ida_volta():
    for kg in (0.0, 1.0, 65.5):
        lb = core.kg_para_lb(kg)
        kg2 = core.lb_para_kg(lb)
        assert approx(kg, kg2)

# def test_celsius_para_fahrenheit_errado():
#     """Teste propositalmente errado: 0 °C NÃO é 100 °F."""
#     valor = core.celsius_para_fahrenheit(0)
#     assert valor == 100  # deveria ser 32, mas estamos forçando a falha
# # #Alte