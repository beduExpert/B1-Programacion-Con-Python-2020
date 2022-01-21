
## Tests sobre clases y métodos

### OBJETIVO

- Crear test para métodos

#### REQUISITOS

1. Pytest
2. Python 3

#### DESARROLLO

Hasta el momento hemos visto ejemplos de test unicamente con funciones, pero cuando trabajamos usando el paradigma orientado a objetos también se puede realizar tests unitarios, en estos casos la unidad básica a testear son los métodos de clase y se realiza de una manera similar  a cuando se testean funciones.

Por ejemplo, si tenemos la siguiente definición de clase :
```
import json

class EstudianteDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self,nombre):
        for estudiante in self.__data['estudiantes']:
            if estudiante ['nombre'] == nombre:
                return estudiante

```
La cual tiene métodos para conectarse a una base de datos json de estudiantes y devolver datos, si tenemos el siguiente json de prueba
```
{
    "estudiantes": [
        {
            "id": 1,
            "nombre": "Mario",
            "resultado": "aprobado"
        },
        {
            "id": 2,
            "nombre": "Luigi",
            "resultado": "reprobado"
        }
    ]
}
```
Pdemos crear el siguiente test para el método get_data
```
from estudiante import EstudianteDB
import pytest

def test_datos_luigi():
    db = EstudianteDB()
    db.connect('data.json')
    luigi = db.get_data('Luigi')
    assert luigi['id'] == 2
    assert luigi['nombre'] == 'Luigi'
    assert luigi['resultado'] == 'reprobado'

def test_datos_mario():
    db = EstudianteDB()
    db.connect('data.json')
    luigi = db.get_data('Mario')
    assert luigi['id'] == 1
    assert luigi['nombre'] == 'Mario'
    assert luigi['resultado'] == 'aprobado'
```
Al ejecutar este test, podemos ver que el método lo pasa
```
$pytest -v test_estudiante.py 
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-05/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-05
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 2 items                                                                                                                                                                                   

test_estudiante.py::test_datos_luigi PASSED                                                                                                                                                   [ 50%]
test_estudiante.py::test_datos_mario PASSED   
```
Él código anterior tiene el problema que para cada prueba, necesita generar una instancia nueva de la clase y reconectarse a la base de datos, esto se puede evitar usando las siguientes funciones:
- setup_module(), se ejecuta antes de los test, aquí podemos crear objetos o conectarnos a bases de datos
- teardown_module() se ejecuta después de los tests, aqui podemos cerrar conexiones o archivos

Por ejemplo el código anterior se puede convertir en el siguiente:
```
from estudiante import EstudianteDB
import pytest

db = None
def setup_module(module):
    global db 
    db = EstudianteDB()
    db.connect('data.json')

#teardown_module sirve para acciones que de realizan al final
#def teardown_module(module):


def test_datos_luigi():
    luigi = db.get_data('Luigi')
    assert luigi['id'] == 2
    assert luigi['nombre'] == 'Luigi'
    assert luigi['resultado'] == 'reprobado'

def test_datos_mario():
    luigi = db.get_data('Mario')
    assert luigi['id'] == 1
    assert luigi['nombre'] == 'Mario'
    assert luigi['resultado'] == 'aprobado'
```
Al ejecutar este test,tenemos el siguiente resultado.
```
$ pytest -v test_estudiante2.py 
======================================================================================== test session starts ========================================================================================
platform linux -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /home/luisams/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-05/.hypothesis/examples')
rootdir: /home/luisams/Documentos/bedu/B1-Programacion-Con-Python-2020/Sesion-08/Ejemplo-05
plugins: doctestplus-0.5.0, arraydiff-0.3, astropy-header-0.1.2, hypothesis-5.5.4, remotedata-0.3.2, openfiles-0.4.0
collected 2 items                                                                                                                                                                                   

test_estudiante2.py::test_datos_luigi PASSED                                                                                                                                                  [ 50%]
test_estudiante2.py::test_datos_mario PASSED    
```