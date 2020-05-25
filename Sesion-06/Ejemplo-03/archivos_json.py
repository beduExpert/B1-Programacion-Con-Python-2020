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
