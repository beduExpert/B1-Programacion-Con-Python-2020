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