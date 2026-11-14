"""Ejecutar desde la carpeta ejemplos: python -m pytest -v"""
import pytest
from importlib import import_module
CuentaBancaria = import_module("07_cuenta_bancaria").CuentaBancaria

@pytest.fixture
def cuenta():
    return CuentaBancaria("Ana", 100)

def test_saldo_inicial(cuenta):
    assert cuenta.saldo == 100

@pytest.mark.parametrize("cantidad,esperado", [(10, 110), (25, 125), (1, 101)])
def test_depositar(cuenta, cantidad, esperado):
    assert cuenta.depositar(cantidad) == esperado

def test_retirar(cuenta):
    assert cuenta.retirar(40) == 60

def test_saldo_insuficiente(cuenta):
    with pytest.raises(ValueError):
        cuenta.retirar(101)

def test_no_depositar_cero(cuenta):
    with pytest.raises(ValueError):
        cuenta.depositar(0)
