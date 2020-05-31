import operaciones

def test_suma():
    assert operaciones.suma(2,3) ==5
    assert operaciones.suma(2)==2

def test_producto():
    assert operaciones.producto(3,5) == 15
    assert operaciones.producto(2) == 2

