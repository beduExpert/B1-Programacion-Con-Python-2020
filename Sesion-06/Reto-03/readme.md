## Reto 3

### OBJETIVO

- Crear archivos json incluyendo datos de la ejecución del programa

#### REQUISITOS

1. Python 3

#### DESARROLLO


`info_archivos.py`

Crear un script de Python que permita conocer una lista de archivos en el directorio, mostrado en pantalla con formato JSON.

Utiliza la librería `os` para obtener una lista de archivos y su información.

El JSON deberá incluir los siguientes elementos: nombre, tamaño, fecha de modificación.



```python
$ python info_archivos.py 
[
    {
        "tamanio": 741, 
        "nombre": "info_archivos.py", 
        "fecha": "Fri Aug  2 01:39:51 2019"
    }, 
    {
        "tamanio": 330, 
        "nombre": "readme.md", 
        "fecha": "Fri Aug  2 01:16:45 2019"
    }
]
```
<details>
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
</details>