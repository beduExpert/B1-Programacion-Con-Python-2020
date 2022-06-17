
## Parametrización de test

### OBJETIVO

- Crear test con argumentos parametrizados

#### REQUISITOS

1. Pytest
2. Python 3

#### DESARROLLO

Cómo hemos visto anteriormente es posible crear múltiples tests para la misma funciónm y cada uno de estos puede tener distintos asserts, por ejemplo:

```
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
```
Pero ésta forma puede tener el problema de ser muy repetitiva al momento de escribir código.

Otra forma de escribir este set de pruebas, utiliza el mark parametrize, que recibe como argumentos:
- Una cadena con el nombre de los parámetros
- Una lista que tenga los parámetros en tuplas

Los parámetros deben proporcionarse a la función test

El mismo set de pruebas utilizando parametros queda de esta manera
```
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


```

El resultado al ejecutar
```
$pytest test_operaciones_param.py -v
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-04/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-04
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 5 items                                                                                                                                                                                   

test_operaciones_param.py::test_suma[2-3-5] PASSED                                                                                                                                            [ 20%]
test_operaciones_param.py::test_suma[2-0-2] PASSED                                                                                                                                            [ 40%]
test_operaciones_param.py::test_suma[Hola -Mundo-Hola Mundo] PASSED                                                                                                                           [ 60%]
test_operaciones_param.py::test_suma[3.1-3.1-6.2] PASSED                                                                                                                                      [ 80%]
test_operaciones_param.py::test_suma[12.5-1.2-13.7] PASSED  
```