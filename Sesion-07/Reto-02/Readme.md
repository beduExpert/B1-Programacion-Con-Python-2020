
## Titulo del Ejemplo 

### OBJETIVO 

- Utilizar rutas con argumentos validados

#### REQUISITOS 

1. Python 3
2. Flask

#### DESARROLLO

- Crea un programa de calculadora similar al reto anterior(suma, resta, multiplicación división)
- El programa debe aceptar los siguientes dos formatos para cada operación
	- http://127.0.0.1:5000/calcula/5+4
	- http://127.0.0.1:5000/calcula/5mas4
- Si falta el segundo número debera obviar un 0(suma, resta) o un 1(multiplicación, división)
- Se debe validar que los parámetros sean números enteros



<details>
	Programa

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
		
</details> 

Agrega una imagen dentro del ejemplo o reto para dar una mejor experiencia al alumno (Es forzoso que agregages al menos una)

![imagen](https://picsum.photos/200/300)

