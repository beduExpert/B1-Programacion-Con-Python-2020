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