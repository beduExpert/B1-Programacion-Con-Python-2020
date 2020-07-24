class Lista_de_compra:
    def __init__(self, *args):
        self.__lista = list()
        for arg in args:
            self.__lista.append(arg)


    def agrega(self, *args):
        for arg in args:
            self.__lista.append(arg)
    
    def imprime(self):
        print("LISTA DE COMPRA")
        for articulo in self.__lista:
            print(articulo)

    def borra(self, *args):
        for arg in args:
            self.__lista.remove(arg)



supermercado = Lista_de_compra('Jamon', 'Queso', 'Pan')
supermercado.agrega('leche', 'huevo')
supermercado.borra('Queso')
supermercado.imprime()

    

