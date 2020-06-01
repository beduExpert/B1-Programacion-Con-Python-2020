from promedio import promedio
import pytest

@pytest.mark.parametrize('num1, num2, resultado',[
                    (2,3,2.5),
                    (2,0,1),
                    (2,4,3),
                    (10,11,10.5),
                    (10.1,10.3,10.2),
                    (1,1,1),
                    (6.0,6.5,6.25,),
                    (15,10,12.5),
                    (0,0,0),
                    (6,5.5,5.75)
                ])
def test_promedio(num1,num2,resultado):
    res = promedio(num1,num2)
    assert res == resultado
    assert type(res) is float

