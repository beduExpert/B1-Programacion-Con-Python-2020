
## Rutas avanzadas

### OBJETIVO

- Crear páginas con múltiples rutas
- Incluir parámetros en las rutas

#### REQUISITOS

1. Python 3
2. Flask

#### DESARROLLO

No siempre queremos que el formato de la ruta de nuestra página sea como las vistas en el ejemplo pasado, por ejemplo puede ser que queramos que el formato de nuestra ruta sea el siguiente:
```
http://127.0.0.1:5000/nombre/param1/param2
```

Lo cual es mucho mas legible

Un ejemplo de este tipo de ruta la podemos lograr con el siguiente decorador:
```
@app.route('/parametros/<nombre>')

```
Además podemos generar múltiples decoradores sobre un mismo método, lo cual puede ser útil en caso de que no se otorgue la totalidad de parámetros-

```
@app.route('/parametros')
@app.route('/parametros/<nombre>')
@app.route('/parametros/<nombre>/<edad>')
```
En caso de que necesitemos que uno de los datos recibidos no sea de tipo string, podemos indicarlo en el decorador.
```
@app.route('/parametros/<nombre>/<int:edad>')
```
Los mismos parámetros dados en el decorador deben especificarse como entradas del método.

```
@app.route('/parametros')
@app.route('/parametros/<nombre>')
@app.route('/parametros/<nombre>/<int:edad>')
def recibe_parametros(nombre="humano", edad = 0):
    return ("nombre   {}\n edad    {} años".format(nombre,edad))

```

El código completo del ejemplo es el siguiente:
```
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Programa de ejemplo"

@app.route('/parametros')
@app.route('/parametros/<nombre>')
@app.route('/parametros/<nombre>/<int:edad>')
def recibe_parametros(nombre="humano", edad = 0):
    return ("nombre   {}\n edad    {} años".format(nombre,edad))


if __name__ == "__main__":
    app.run(debug=True)
```
Al ejecutar el servidor y entrar a las siguientes rutas tenemos las siguientes salidas
- http://127.0.0.1:5000/parametros/luis/8   nombre luis edad 8años
- http://127.0.0.1:5000/parametros/karla  nombre karla edad 0 años
- http://127.0.0.1:5000/parametros nombre humano edad 0 años
- http://127.0.0.1:5000/parametros/lalo/nueve ERRROR

