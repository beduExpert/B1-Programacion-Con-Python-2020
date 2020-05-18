#Importamos modulo que posee clases para fecha
import datetime

#Se crea un objeto date con fechas determinadas
fecha = datetime.date(1937, 10, 8)  #year, month, day
print(fecha)

#Al preguntar el tipo del objeto devuelve clase fecha
print(type (fecha))

#Podemos acceder a atributos dentro del objeto
mes = fecha.month
anyo = fecha.year
print("el mes es:" , mes)
print("el año es ", anyo)

#Las clases también contienen métodos, o funciones asociadas al comportamiento de la clase
print(fecha.strftime("%b %d %Y %H:%M:%S")) #Devuelve una cadena de texto con la fecha
