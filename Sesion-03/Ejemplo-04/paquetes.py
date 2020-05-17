#Se pueden importar modulos contenidos dentro del paquete
import matematicas.otros
matematicas.otros.tabla(2)

#Tambien asi
from matematicas import aritmetica
print(aritmetica.suma(4,3))

#Importar solo una funcion
from matematicas.aritmetica import promedio
print(promedio(2,3))