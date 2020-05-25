import os
import json
from datetime import datetime

def obtiene_archivos(d):
    archivos = os.listdir(d)

    archivos = [
        {
            "nombre": a,
            "tamanio": os.path.getsize(os.path.join(d,a)),
            "fecha": os.path.getmtime(os.path.join(d,a)),
        }
        for a in archivos
    ]

    for archivo in archivos:
        fecha = datetime.fromtimestamp(archivo['fecha'])
        archivo['fecha'] = fecha.strftime("%c")


    return archivos

def imprime_archivos(archivos):
    archivos_json = json.dumps(archivos, indent=4)
    print(archivos_json)


archivos = obtiene_archivos(".")
imprime_archivos(archivos)