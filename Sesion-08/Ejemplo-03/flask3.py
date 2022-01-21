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