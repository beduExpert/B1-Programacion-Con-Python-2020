 
	
## Calculadora web 

### OBJETIVO 
Crear una página 

#### REQUISITOS 

1. Python 3
2. Flask

#### DESARROLLO

- Crea una página capas de calcular la suma, resta o multiplicación de dos números
- Tanto la operación como los números se deben ingresar como parámetros dentro de la ruta

Ejemplo:
http://127.0.0.1:5000/calculadora?operacion=suma&n1=10&n2=4

Pista:Puedes utilizar varias veces request para tener distintos parametros

<details>
	Codigo

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
</details> 

Agrega una imagen dentro del ejemplo o reto para dar una mejor experiencia al alumno (Es forzoso que agregages al menos una)

![imagen](https://picsum.photos/200/300)

