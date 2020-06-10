from flask import Flask, render_template
from datos import base_de_usuarios

app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def index():
    titulo = 'Reporte de clientes'
    return render_template('index.html', title = titulo, clientes = base_de_usuarios)

@app.route('/usuario=<nombre>')
def usuario(nombre):
    titulo = 'Reporte del cliente: {}'.format(nombre)
    indice = 0
    for _ in base_de_usuarios:
        if base_de_usuarios[indice].get_nombre() == nombre:
            val = indice
        indice +=1
    tarjetas_usuario = base_de_usuarios[val].get_tarjetas()    
    return render_template('cliente.html', title = titulo, tarjetas = tarjetas_usuario, usuario = str(val))

@app.route('/usuario=<int:nombre>/tarjeta=<tarjeta>')
def reporte(nombre, tarjeta):
    usser = base_de_usuarios[nombre]
    indice = 0
    val = 99
    for tarj in usser.get_tarjetas():
        if tarj.get_nombre() == tarjeta:
            val = indice
        indice +=1
    lista_tarjetas = usser.get_tarjetas()
    texto = lista_tarjetas[val].get_reporte_html()
    return(texto)

@app.route('/gen_usuario=<int:nombre>')
def reporte_general(nombre):
    usser = base_de_usuarios[nombre]
    texto = usser.get_reportes_html()
    return(texto)
if __name__ == "__main__":
    app.run(debug=True)
