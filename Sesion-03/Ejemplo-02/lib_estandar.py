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
