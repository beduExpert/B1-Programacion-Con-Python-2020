from flask import Flask, render_template, url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Programa de calculadora"



@app.route('/calculadora')
def saluda():
    operacion = request.args.get('operacion', 'mas')
    n1 = request.args.get('n1', '0')
    n2 = request.args.get('n2', '0')
    if operacion == "mas":
        res = int(n1) + int(n2)
    elif operacion == "menos":
        res = int(n1) - int(n2)
    elif operacion == "por":
        res = int(n1) * int(n2)
    elif operacion == "entre":
        res = int(n1) / int(n2)
    return "{} {} {} es {}".format(n1,operacion,n2,res)


if __name__ == "__main__":
    app.run(debug=True)