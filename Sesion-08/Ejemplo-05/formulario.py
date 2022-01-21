from wtforms import Form 
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

class Formulario_usuario(Form):
    usuario = StringField("Usuario")
    correo = EmailField ("Correo electrónico")
    comentario = TextField("Comentario")
