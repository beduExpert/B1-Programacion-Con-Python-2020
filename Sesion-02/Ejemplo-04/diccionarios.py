
# Creando diccionarios  
d1 = {}
d2 = dict() 

print(type(d1) )

#Crear diccionario con datos
d3 = {"Usuario": "usser123", "Correo": "us12@bedu.org", "Compañia": "Bedu"} 

#Observe los pares en formatollave:valor     
print(d3)

# Se pueden obtener las llaves en una lista
print(d3.keys()) 

# Se pueden obtener los valores en una lista
print(d3.values()) # Lista de valores

#Se pueden agregar entradas en un diccionario
d3['ciudad']= "CDMX"
print(d3)

#Se puede acceder a los valores del diccionario usando su llave
print(d3['ciudad'])

#Tambien podemos extraer datos usando pop
a = d3.pop('ciudad')
print(a)
print(d3)