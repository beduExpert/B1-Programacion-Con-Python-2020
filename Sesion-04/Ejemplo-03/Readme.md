

## Encapsulación

### OBJETIVO

- Definir elementos de clase privados

#### REQUISITOS

1. Python 3

#### DESARROLLO

La encapsulación consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior.
En algunos lenguajes, estos se conoce como elementos privados.

En Python no existe, pero se puede simular precediendo atributos y métodos con dos barras bajas __ como indicando que son "especiales".

```python
#Definicion de clase con atributos y métodos privados
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."
    def get_atributo(self):
        return self.__atributo_privado
    def __metodo_privado(self):
        return "Metodo privado ejecutivo"
    def metodo_publico(self):
        print(self.__metodo_privado())

e = Ejemplo()
#El ejecutar la siguiente linea, causa error debido a que se intenta el acceso a un atributo privado
#print(e.__atributo_privado)

#Pero si se puede hacer a travez de un método publico
print(e.get_atributo())

#El ejecutar la siguiente linea, causa error debido a que se intenta el acceso a un método privado
#e.__metodo_privado()

#Pero si se puede hacer a travez de un método publico
e.metodo_publico()
```

Los atributos privados, también pueden proteger valores que no deseamos que sean editados por fuera.
Por ejemplo, en una clase de una cuenta bancaria, no esperaríamos que alguien manipule externamente el saldo.

```python
class Cuenta:
    saldo = 5000

    def saldo(self):
        return self.__saldo

cheques = Cuenta()
cheques.__saldo = 100000  # Sin efecto
print(cheques.saldo())

```

