from flask import Flask
from flask import render_template
from flask import request
import formulario

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
    form_usuario = formulario.Formulario_usuario(request.form)
    titulo = "Modulo Flask"
    if request.method == 'POST':
        print (form_usuario.usuario.data)
        print (form_usuario.correo.data)
        print (form_usuario.comentario.data)
    return render_template('index.html', title = titulo, form = form_usuario)

if __name__ == "__main__":
    app.run(debug=True)

