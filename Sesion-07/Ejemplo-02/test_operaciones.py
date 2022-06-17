import operaciones

def test_suma():
    assert operaciones.suma(2,3) ==5
    assert operaciones.suma(2)==2

def test_producto():
    assert operaciones.producto(3,5) == 15
    assert operaciones.producto(2) == 2

def test_suma_string():
    resultado = operaciones.suma('Hola ', 'Mundo')
    assert resultado == 'Hola Mundo'
    assert type(resultado) is str
    assert len(resultado) > 0

def test_producto_string():
    resultado = operaciones.producto('Hola ', 3)
    assert resultado == 'Hola Hola Hola '

