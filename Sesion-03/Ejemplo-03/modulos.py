#Se importa el paquete completo
import aritmetica
print(aritmetica.promedio(1,3,5))

#importar una función desde el paquete
from aritmetica import suma
print(suma(1,3,5))

#Usar alias para elementos importados
from aritmetica import producto as prod
print(prod(1,2))