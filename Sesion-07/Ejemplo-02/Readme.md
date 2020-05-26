
agrega el programa que se desarrollara con backticks> [agrega la sesion con backticks]

## Titulo del Ejemplo

### OBJETIVO

- Incluir Jinja en nuestras plantillas
- Incluir estilos en nuestras páginas web usando archivos css

#### REQUISITOS

1. Python 3
2. Flask

#### DESARROLLO

Jinja 2 es un motor de plantillas para Python, lo que significa que le permite al desarrollador producir páginas web, que contienen, por ejemplo, código html base y marcadores de posición para que Jinja 2 los llene. Basado en el sistema de plantillas de Django, Jinja es uno de los más utilizados, ya que permite a los desarrolladores usar conceptos poderosos como sandboxing y herencia para permitir que una plantilla se reutilice fácilmente.
 
Jinja nos permite usar bloques con la siguiente forma, y expandirlo desde otro archivo.
```
{% block body %} {% endblock %}
```
```
{% block body %} 
<h1>
    PARTE 2
</h1>
{% endblock %}
```

En el ejemplo de esta carpeta puedes ver como el archivo extender.html inserta dentro de pagina.html usando jinja

Otro tipo de bloques jinja es el delimitado por {{ }}, los cuales nos permiten insertar código dentro de los html

```
    <link rel="stylesheet" href="{{ url_for('static', filename = 'css/main.css')}}">

```
archivo pagina.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename = 'css/main.css')}}">
    {% block head %} {% endblock %}

</head>
<body>

    {% block body %} {% endblock %}
</body>
</html>
```

extender.html

```
{% extends 'pagina.html' %}
{% block head %}

{% endblock %}

{% block body %} 
<h1>
    PARTE 2
</h1>
{% endblock %}
```


Los archivos css (hojas de estilos en cascada) nos permiten incluir plantillas de estilos  para definir y crear la presentación de un documento estructurado escrito en html.

Coloca los archivos css en la carpeta static y no olvides linkearlos a la página.

Ejemplo de archivo css
```
body{
    margin:0;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    color:green;
    
}
```
Si ejecutas flask3.py en un navegador verás que la hoja de estilos habrá modificado el color y fuente del texto en el body.




