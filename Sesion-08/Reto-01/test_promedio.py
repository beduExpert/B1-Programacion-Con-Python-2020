from promedio import promedio

def test_promedio():
    assert promedio(2,4) == 3
    assert promedio(10,11) == 10.5
    assert promedio(4,4) == 4
