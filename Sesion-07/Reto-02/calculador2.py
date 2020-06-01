from flask import Flask, render_template, url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Programa de calculadora"


@app.route('/calcula/<int:num1>+<int:num2>')
@app.route('/calcula/<int:num1>mas<int:num2>')
@app.route('/calcula/<int:num1>mas')
@app.route('/calcula/<int:num1>+')
def suma(num1=0, num2=0):
    res = num1+num2
    return str(res)
    

@app.route('/calcula/<int:num1>-<int:num2>')
@app.route('/calcula/<int:num1>menos<int:num2>')
@app.route('/calcula/<int:num1>menos')
@app.route('/calcula/<int:num1>-')
def resta(num1=0, num2=0):
    res = num1-num2
    return str(res)    

@app.route('/calcula/<int:num1>*<int:num2>')
@app.route('/calcula/<int:num1>por<int:num2>')
@app.route('/calcula/<int:num1>por')
@app.route('/calcula/<int:num1>*')
def multi(num1=0, num2=1):
    res = num1*num2
    return str(res) 

@app.route('/calcula/<int:num1>/<int:num2>')
@app.route('/calcula/<int:num1>entre<int:num2>')
@app.route('/calcula/<int:num1>/')
@app.route('/calcula/<int:num1>entre')
def divide(num1=0, num2=1):
    res = num1/num2
    return str(res) 

if __name__ == "__main__":
    app.run(debug=True)