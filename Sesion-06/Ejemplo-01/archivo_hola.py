# Escribiendo un archivo 

archivo = open("hola.txt", "w") # w para escritura

archivo.write("Primer linea de este archivo\n")
archivo.writelines(["Multiples ", "Linea\n", "En ", "Lista"])
archivo.close() # Debemos cerrar el archivo

# Leyendo un archivo
archivo = open("hola.txt", 'r')

a = archivo.readline()  #Lee una linea de archivo
print(a)
b = archivo.readlines() #Devuelve el archivo en una lista
print(b)
archivo.close()

#Durante la lectura podemos iterar por linea el archivo
f = open("hola.txt", "r")
for linea in f:
    print(linea)
f.close()

