import operaciones
import pytest

@pytest.mark.parametrize('num1, num2, resultado',[
                    (2,3,5),
                    (2,0,2),
                    ('Hola ', 'Mundo', 'Hola Mundo'),
                    (3.1, 3.1, 6.2),
                    (12.5, 1.2, 13.7)
                ])
def test_suma(num1, num2, resultado):
    assert operaciones.suma(num1, num2)==resultado 

