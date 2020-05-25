## Manipulación de archivos

### OBJETIVO

- Crear archivos de texto nuevos
- Leer archivos de texto
- Escribir archivos de texto
- Usar with en archivos

#### REQUISITOS

1. Python 3

#### DESARROLLO

Los archivos en Python son objetos tipo *file* creados mediante la función *open* (abrir). Toma como parámetros una cadena con la ruta, y 2 opcionales, modo de acceso y tamaño de búfer.

`archivo_hola.py`
```
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


```

### El comando with

A pesar de que podemos utilizar archivos como el ejemplo anterior, se recomienda utilizar el comando *with*, que automaticamente cierra el archivo una vez dejemos de utilizar. Para ellos debemos indentar en un bloque su uso:

`hola_with.py`
```

#La sentencia with coloca la lectura o escritura del archivo en una estructura que lo cierra al terminar
with open("arch2.txt", 'w') as archivo: 
    archivo.write("Primer linea de este archivo\n") 
    archivo.writelines(['Multiples Lineas\n', 'En Lista']) 
                                                                                                                                                 
with open("arch2.txt", 'r') as archivo: 
    print(archivo.readline()) 
    print(archivo.readlines())  
```
