## Json

### OBJETIVO

- Convertir diccionarios a formato json y viceversa
- Escribir/Leer archivos .json

#### REQUISITOS

1. Python 3

#### DESARROLLO
JSON (JavaScript Object Notation), es un formato basado en texto, utilizado para transmitir y almacenar información estruturada. Es muy utilizado en diversas herramientas web. Guarda cierta similitud con los diccionarios de Python.


`usa_json.py`
import json

#En python los diccionarios pueden convertirse a json y viceversa

mi_dic = {"nombre": "Armando", "apellido": "Armada", "lista": [1,2,3,4]}

 # Conviertelo a string en formato JSON
mi_js = json.dumps(mi_dic) 
print(mi_js)

#Convertir un json a diccionario
mi_json = """{"nombre": "Caballero", "apellido": "Caballo", "lista": [5,6,7,8]}"""
json.loads(mi_json) # De string JSON a diccionario

mi_json = """{"nombre": "Caballero", "apellido": "Caballo", "lista": [5,6,7,8]}""" 

dic = json.loads(mi_json) # De string JSON a diccionario
print(dic)

print(dic['nombre'])
```

### Elementos similares en JSON y diccionarios

Los elementos de un diccionario de Python, son convertidos al tipo de dato mas cercano en JavaScript, y viceversa.

[Equivalencias](./elementos.png)

### Archivos JSON

La 's' en los comandos de json (load**s** y dump**s**), indican que se trata de un string. También podemos manejar archivos mediante *load* y *dumps*

`archivos_json.py`
```
import json 
from datetime import datetime

#Se pueden convertir diccionarios a json y guardarlos en archivos .json

with open("ejemplo.json", "w") as fjson: # Guardarlo como archivo
   mi_dicc = {"nombre": "diccionario", "year": 2019} 
   json.dump(mi_dicc, fjson, indent=4)  


with open("ejemplo2.json", "w") as fjson: 
    mi_dicc = {"fecha": datetime.now().strftime("%c")} # Las fechas necesitan convertirse 
    json.dump(mi_dicc, fjson, indent=4)  # Puede agregarse indentación

with open("ejemplo2.json", 'r') as fjson: 
    mi_json = json.load(fjson) 
    print(mi_json) 
                                                                                                                                                        
{'fecha': 'Fri Aug  2 00:25:46 2019'}

```