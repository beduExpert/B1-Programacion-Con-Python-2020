import operaciones
import pytest

def test_suma():
    assert operaciones.suma(2,3) ==5
    assert operaciones.suma(2,0)==2


def test_suma_string():
    resultado = operaciones.suma('Hola ', 'Mundo')
    assert resultado == 'Hola Mundo'

def test_suma_float():
    assert operaciones.suma(3.1,3.1)==6.2
    assert operaciones.suma(12.5,1.2)==13.7
