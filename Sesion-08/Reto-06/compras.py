class Lista_de_compra:
    def __init__(self, *args):
        self.__lista = list()
        for arg in args:
            self.__lista.append(arg)
        return self.__lista


    def agrega(self, *args):
        for arg in args:
            self.__lista.append(arg)
        return self.__lista
    
    def imprime(self):
        print("LISTA DE COMPRA")
        for articulo in self.__lista:
            print(articulo)
        return self.__lista


    def borra(self, *args):
        for arg in args:
            self.__lista.remove(arg)
        return self.__lista



