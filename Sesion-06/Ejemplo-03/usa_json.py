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
