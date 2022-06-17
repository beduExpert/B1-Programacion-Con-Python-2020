from promedio import promedio

def test_promedio_int():
    resultado = promedio(2,4)
    assert resultado == 3
    assert type(resultado) is float
    resultado = promedio(10,11)
    assert resultado == 10.5
    assert type(resultado) is float


def test_promedio_float():
    resultado = promedio(10.1,10.3)
    assert resultado == 10.2
    assert type(resultado) is float
    resultado = promedio(6.0 ,6.5)
    assert resultado == 6.25
    assert type(resultado) is float
