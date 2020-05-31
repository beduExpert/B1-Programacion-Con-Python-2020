
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Titulo del Ejemplo

### OBJETIVO

- Se utilizarán distintas opciones para filtrar que funciones test se ejecutaran

#### REQUISITOS

1. Pytest
2. Python 3

#### DESARROLLO

Además de ejecutar de forma directa una función test, podemos usar -k para filtrar los test por nombre, por ejemplo podemos ejecutar los test que incluyen suma.

```
$pytest -k "suma" -v
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items / 2 deselected / 2 selected                                                                                                                                                       

test_operaciones.py::test_suma PASSED                                                                                                                                                         [ 50%]
test_operaciones.py::test_suma_string PASSED                                                                                                                                                  [100%]

================================================================================== 2 passed, 2 deselected in 0.02s ==================================================================================
```
De forma similar podemos usar and y or para manipular nuestos filtros

```
$pytest -k "suma or string" -v
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items / 1 deselected / 3 selected                                                                                                                                                       

test_operaciones.py::test_suma PASSED                                                                                                                                                         [ 33%]
test_operaciones.py::test_suma_string PASSED                                                                                                                                                  [ 66%]
test_operaciones.py::test_producto_string PASSED                                                                                                                                              [100%]

================================================================================== 3 passed, 1 deselected in 0.02s ==================================================================================
```

Al importar el módulo pytest en nuestro código podemos utilizar el decorador mark para crear una marca que nos permita filtrar posteriormente nuestros tests

```
import operaciones
import pytest

@pytest.mark.numero
def test_suma():
    assert operaciones.suma(2,3) ==5
    assert operaciones.suma(2)==2

@pytest.mark.numero
def test_producto():
    assert operaciones.producto(3,5) == 15
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
```

Para filtrar usando marks, podemos utilizar -m
```
pytest -m numero -v
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items / 2 deselected / 2 selected                                                                                                                                                       

test_operaciones.py::test_suma PASSED                                                                                                                                                         [ 50%]
test_operaciones.py::test_producto PASSED   
```
Generalmente, se ejecutaran todos los tests sin importar si alguno resulta en un error, pero en caso de que queramos que al momento de fallar uno de los tests la prueba se detenga, podemos usar -x

En el siguiente ejemplo modificamos el programa para que falle en el segundo test.

Si no usamos -x obtenemos:
```
$pytest -v 
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items                                                                                                                                                                                   

test_operaciones.py::test_suma PASSED                                                                                                                                                         [ 25%]
test_operaciones.py::test_producto FAILED                                                                                                                                                     [ 50%]
test_operaciones.py::test_suma_string PASSED                                                                                                                                                  [ 75%]
test_operaciones.py::test_producto_string PASSED                                                                                                                                              [100%]

============================================================================================= FAILURES ==============================================================================================
___________________________________________________________________________________________ test_producto ___________________________________________________________________________________________

    @pytest.mark.numero
    def test_producto():
>       assert operaciones.producto(3,5) == 16
E       assert 15 == 16
E         -15
E         +16

test_operaciones.py:11: AssertionError
```
Al contrario, usar -x nos permite hacer que la ejecución de los tests se detenga al fallar uno.

```
pytest -v -x
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items                                                                                                                                                                                   

test_operaciones.py::test_suma PASSED                                                                                                                                                         [ 25%]
test_operaciones.py::test_producto FAILED                                                                                                                                                     [ 50%]

============================================================================================= FAILURES ==============================================================================================
___________________________________________________________________________________________ test_producto ___________________________________________________________________________________________

    @pytest.mark.numero
    def test_producto():
>       assert operaciones.producto(3,5) == 16
E       assert 15 == 16
E         -15
E         +16

test_operaciones.py:11: AssertionError
```
De froma similar podemos utilizar --maxfail para colocar un límite de test fallados antes de abortar la ejecución

```
$pytest -v --maxfail=2
```
Otra forma de saltar un test, por ejemplo en el caso de que aún se encuentre en desarrollo, es usar la marca skip. Por ejemplo
```
@pytest.mark.skip(reason="no ejecutes este test")
def test_suma_string():
    resultado = operaciones.suma('Hola ', 'Mundo')
    assert resultado == 'Hola Mundo'
    assert type(resultado) is str
    assert len(resultado) > 0
```
```
ytest test_operaciones_salta.py 
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items                                                                                                                                                                                   

test_operaciones_salta.py ..s.                                                                                                                                                                [100%]

=================================================================================== 3 passed, 1 skipped in 0.03s ====================================================================================
(base) luisams@luisams-Inspiron-3459:~/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03$ pytest test_operaciones_salta.py -v
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-03
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items                                                                                                                                                                                   

test_operaciones_salta.py::test_suma PASSED                                                                                                                                                   [ 25%]
test_operaciones_salta.py::test_producto PASSED                                                                                                                                               [ 50%]
test_operaciones_salta.py::test_suma_string SKIPPED                                                                                                                                           [ 75%]
test_operaciones_salta.py::test_producto_string PASSED                                                                                                                                        [100%]

=================================================================================== 3 passed, 1 skipped in 0.02s ====================================================================================
```
De forma similar si se requiere saltar un test bajo una condición, se puede usar la marca skipif(condicion) para decorar el test

