#Las funciones son porciones de código que se pueden llamar para hacer uso de su codigo

#Algunas que ya hemos utilizado
print("Hola Mundo")
#input()

#Para definirlas usamos def
def hola_mundo():
    print("Hola Mundo")
#Para llamarlas, lo hacemos por su nombre
hola_mundo()

#Las funciones pueden tener parámetros
def saludo(persona):
    print("Hola {}".format(persona))

#Podemos repetir el mismo comportamiento con distintos parámetros
saludo("Luis")
saludo("Karla")
saludo("Mundo")

#Las funciones pueden devolver algun dato
def area_rectangulo(base, altura):
    area = base * altura
    return area

b = 5
h = 3
area = area_rectangulo(b, h)
print("El área de un rectangulo de {} * {} es {}".format(b,h,area))


