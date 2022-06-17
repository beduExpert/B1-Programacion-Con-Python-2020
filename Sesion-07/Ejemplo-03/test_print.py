def suma(a, b):
    return a + b

def test_suma():
    a = 15
    b = 5
    print(f"Valor de a: {a}")
    print(f"Valor de b: {b}")
    c = suma(a, b)
    print(f"Resultado suma: {c}")
    assert c == a + b
