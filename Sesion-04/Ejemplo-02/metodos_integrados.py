class MiClase():
    def __init__(self):
        print("Objeto de clase MiClase creado")
    
    def __del__(self):
        print("Objeto de clase MiClase destruido")
    
    def __str__(self):
        return "Objeto de clase MiClase"

#Llama a __init__
objeto = MiClase()

#Llama a _str__
print(objeto)

#__del__ se llama automaticamente cuando el objeto ya no se utilizará, en este caso al final del programa
