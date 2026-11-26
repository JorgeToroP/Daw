# archivo: test_calculadora.py

from calculadora import sumar, dividir
import pytest

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    
def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5
    
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)