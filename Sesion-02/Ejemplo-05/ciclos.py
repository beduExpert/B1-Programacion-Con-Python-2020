#Los ciclos while repiten el código que se encuentra en su interior mientras se cumpla una condicion
i = 1
while i <= 5:
    print(i)
    i += 1
print("Programa terminado")

#Ten cuidado, si un ciclo for siempre cumple su condicion, nunca se detendra!
"""
while True:
    print("Ciclo sin fin")
"""

#Se pueden usar ciclos for acompañados de range para repetir el interior n veces
for i in range (5):
    print(i)
print("Fin del ciclo")

#En python, los ciclos for nos permiten recorrer estructuras de datos iterables
#Por ejemplo listas
animales = ['gato', 'perro', 'serpiente']
for animal in animales:
    print ("El animal es: {0}, tamaño de palabra es: {1}".format(animal, len(animal)))

#Para diccionarios podemos obtener las llaves y valores y luego recorrerlos

d3 = {"Usuario": "usser123", "Correo": "us12@bedu.org", "Compañia": "Bedu"} 

llaves = d3.keys()
valores = d3.values()
cantidad_datos = d3.items()

for campo, valor in cantidad_datos:
    print("el campo {} contiene: {}".format(campo, valor))
