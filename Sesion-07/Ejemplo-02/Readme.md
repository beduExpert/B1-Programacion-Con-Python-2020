
## Test unitarios avanzados

### OBJETIVO

- Se crearan archivos con múltiples test para una misma función
- Se abordarán opciones al ejecutar tests.

#### REQUISITOS

1. Python 3
2. Pytest

#### DESARROLLO

Al crear tests unitarios se puede establecer condiciones dentro de los assert que no unicamente evaluan la igualdad de la salida de la función con un valor, de hecho dentro de los assert se puede colocar cualquier expresión que devuelva un valor booleano.

Por ejemplo, la siguiente función evalua el uso de la función suma con entradas de tipo str.

```python
def test_suma_string():
    resultado = operaciones.suma('Hola ', 'Mundo')
    assert resultado == 'Hola Mundo'
    assert type(resultado) is str
    assert len(resultado) > 0
```
Además se pueden tener distintas funciones para testear la misma función, por ejemplo
```python
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

```
si ejecutamos pytest sin ningún parametro:
```
$pytest
```
buscará de forma automática los archivos con la forma test_archivo.py y en ellos, las funciones  test_funcion()
```
$pytest
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-02
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items                                                                                                                                                                                   

test_operaciones.py ....                                                                                                                                                                      [100%]

========================================================================================= 4 passed in 0.02s =========================================================================================
```
Si queremos obtener una mayor información, podemos usar la opción -v (verbose), mostrando el resultado individual para cada test.
```
$pytest -v
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-02/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-02
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 4 items                                                                                                                                                                                   

test_operaciones.py::test_suma PASSED                                                                                                                                                         [ 25%]
test_operaciones.py::test_producto PASSED                                                                                                                                                     [ 50%]
test_operaciones.py::test_suma_string PASSED                                                                                                                                                  [ 75%]
test_operaciones.py::test_producto_string PASSED                                                                                                                                              [100%]

========================================================================================= 4 passed in 0.03s =========================================================================================\
```
Se puede seleccionar el archivo de test a ejecutar con la sintaxis vista en el ejemplo anterior, o bien seleccionar una función de test especifica.
```
$pytest test_operaciones.py::test_suma
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-02
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 1 item                                                                                                                                                                                    

test_operaciones.py .                                                                                                                                                                         [100%]

========================================================================================= 1 passed in 0.01s =========================================================================================
```


