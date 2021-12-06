

## Importar modulos de la libreris estandar y de librerias externas

### Objetivo

- Importar modulos de libreria estandar u otras librerías instaladas
- Revisar la instalación de Pip
- Instalar modulos desde Pip
- Importar modulos externos

#### Requisitos

1. Python
2. Pip 
3. Conexión a internet para instalar modulos

#### Desarrollo

Python es un lenguaje con "baterías incluidas", esto significa que contiene paquetes incluidos para comenzar a trabajar con Python, así como un gestor de paquetes, que nos permite agregar mas librerías de forma sencilla. Las librerías contienen código escrito por otras personas, que nos agregan funcionalidad, sin tener que escribirla desde cero, por ejemplo, para leer un archivo CSV.

La libreria estandar contiene una serie de modulos para distintos propositos.

Para utilizar cualquier libería, usamos la palabra reservada import.

```
# Importar modulos desde la libreria estandar
import os 

# Obteniendo ayuda sobre el modulo, usa  q para salir, jk para moverse arriba / abajo

help(os)

# Usa una función que se encuentra en el modulo, en este caso una lista de directorios
files = os.listdir()
print(files)

# Obteniendo el tamaño de un archivo en kB   

size = os.path.getsize('Readme.md')
print(size)

# Otras maneras de importar modulos
import os.path # Solo algun submodulo, llamando os.path
from os import path # Similar, se llama path directamente
from os import path as pt #importa con alias
```
Adicionalmente, Python poseé una gran cantidad de desarrolladores que han creado distintos modulos. Una forma de acceder a este software es por medio de Pip.

Para instalar Pip ve al siguiente enlace.
https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/
(Sigue las instrucciones de acuerdo a tu SO)

Pip nos permite instalar paquetes desde la terminal, puedes buscar paquetes en: https://pypi.org/

Por ejemplo, para instalar Flask ejecuta en la terminal.
```
$pip install flask
```
Ya instalado lo podemos usar con import 
```
#Despues de instalar flask usando pip, lo podemos importar de forma usual
from flask import Flask
app= Flask(__name__)

#Veremos más sobre Flask en próximas lecciones

```
