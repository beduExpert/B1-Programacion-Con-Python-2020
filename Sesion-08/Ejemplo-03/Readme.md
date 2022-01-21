
## Titulo del Ejemplo

### OBJETIVO

- Crear páginas con múltiples rutas
- Incluir argumentos en las rutas

#### REQUISITOS

1. Python 3
2. Flask

#### DESARROLLO

Al usar flask es posible crear páginas con varias rutas con comportamiento independiente, para esto utilizaremos el decorador @app.route sobre distintos métodos

Por ejemplo en el siguiente fragmento de código existen dos rutas.
```
@app.route('/')
def index():
    return render_template('extender.html')

@app.route('/nombre')
def nombre():
    return "Luis"
```
Si esto se ejecuta en un servidor local, al entrar en la ruta http://127.0.0.1:5000/ entraremos a la página correspondiente a la plantilla extender.html, en caso contrario al entrar a http://127.0.0.1:5000/nombre ,  en el navegador se verá una página en blanco con la palabra Luis.

Además de tener múltiples rutas es posible crear páginas que acepten argumentos por medio de la URL, para esto podemos utilizar el método request-

```

@app.route('/saluda')
def saluda():
    nombre = request.args.get('nombre', 'humano')
    return "Hola {}".format(nombre)

```
Al cual hay que pasarle como atributos el nombre del argumento y un valor por defecto. Por ejemplo con el código anterior al entrar a las siguientes direcciones estos son los resultados.

- http://127.0.0.1:5000/saluda -> Hola humano
- http://127.0.0.1:5000/saluda?nombre=Pablo -> Hola Pablo
- http://127.0.0.1:5000/saluda?nombre=Juan -> Hola Juan

El código completo del ejemplo es el siguiente
```
from flask import Flask, render_template, url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('extender.html')

@app.route('/nombre')
def nombre():
    return "Luis"

@app.route('/saluda')
def saluda():
    nombre = request.args.get('nombre', 'humano')
    return "Hola {}".format(nombre)


if __name__ == "__main__":
    app.run(debug=True)
```