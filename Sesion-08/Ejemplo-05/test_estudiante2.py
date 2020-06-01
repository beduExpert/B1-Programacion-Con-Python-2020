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