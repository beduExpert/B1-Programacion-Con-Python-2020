import operaciones
import pytest

@pytest.mark.numero
def test_suma():
    assert operaciones.suma(2,3) ==5
    assert operaciones.suma(2)==2

@pytest.mark.numero
def test_producto():
    assert operaciones.producto(3,5) == 16
    assert operaciones.producto(2) == 2

@pytest.mark.texto
def test_suma_string():
    resultado = operaciones.suma('Hola ', 'Mundo')
    assert resultado == 'Hola Mundo'
    assert type(resultado) is str
    assert len(resultado) > 0

@pytest.mark.texto
def test_producto_string():
    resultado = operaciones.producto('Hola ', 3)
    assert resultado == 'Hola Hola Hola '

