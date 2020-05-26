
## Introduccióm a Flask

### OBJETIVO

- Crear una página utilizando Flask
- Mostrar templates 

#### REQUISITOS

1. Python 3
2. Flask instalado

#### DESARROLLO

Flask es un framework minimalista escrito en Python que permite crear aplicaciones web rápidamente y con un mínimo número de líneas de código. 

Para utilizar flask es necesario instalarlo e importarlo, no está disponible desde la libreria estandar, pero si desde pip

```
pip installl flask
```
Para especificar la ruta que se ejecutara desde una dirección es necesario aplicar un decorador @app.route(ruta).

El siguiente código muestra como crear una página que imprime "Hola Mundo", debido a que index se encuentra decorado con '/', la entrada será directa

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo!"

if __name__ == "__main__":
    app.run(debug=True)% Permite ver opciones de depuración en caso de errores
```

Al ejecutarse este programa muestra en la terminal:
```
 python flask3.py 
 * Serving Flask app "flask3" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 291-567-355
127.0.0.1 - - [26/May/2020 15:29:54] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:31:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:31:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:31:36] "GET /static/css/main.css HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:33:48] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:33:48] "GET /static/css/main.css HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:34:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:34:22] "GET /static/css/main.css HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:34:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [26/May/2020 15:34:23] "GET /static/css/main.css HTTP/1.1" 304 -
```
En el cual nos indica que para ver la página en ejecución debemos ir a: http://127.0.0.1:5000/  en un navegador.

Si en lugar de querer ver un texto en la página queremos mostrar un template .html podemos retornar render_template como en el siguiente ejemplo.
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pagina.html')

if __name__ == "__main__":
    app.run(debug=True)

```

En este caso el código de pagina.html es sencillo.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

</head>
<body>
    Hola Bedu 222
</body>
</html>
```
Recuerda que por default flask busca que el archivo .html se encuentre en la carpeta templates


