from compras import Lista_de_compra
import pytest



def setup_module(module):
    global supermercado, electronicos
    supermercado = Lista_de_compra('Jamon', 'Queso', 'Pan')
    electronicos = Lista_de_compra('computadora')



def test_init():
    assert supermercado is not None
    assert electronicos is not None

def test_agrega():
    assert supermercado.agrega('leche', 'huevo') == ['Jamon', 'Queso', 'Pan','leche', 'huevo' ]
    assert electronicos.agrega('monitor') == ['computadora', 'monitor']

def test_borra():
    assert supermercado.borra('Queso') == ['Jamon', 'Pan','leche', 'huevo' ]
    assert electronicos.borra('monitor', 'computadora') == []

