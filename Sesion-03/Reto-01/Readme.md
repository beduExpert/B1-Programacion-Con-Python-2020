 
	
## Args y kwargs
### OBJETIVO 

- Obtener un numero de argumentos no determinado usando args
- Obtener argumentos con nombre usando kwargs

### REQUISITOS 

1. Python 3 

### DESARROLLO

**Cálculo de IVA**

Vamos a crear funciones para calcular el IVA a diferentes productos, la cual se mejorará progresivamente:

La empresa "Don Panchito SA. de CV.", necesita generar recibos de pago con sus productos, y entre todas las tareas
para generar esos recibos, se te asignó el calculo de IVA. Empecemos con una función sencilla, que irá mejorando a medida
que aumentan las necesidades de la empresa.

1.- La empresa necestia agregar el IVA de 16% a un producto.

**Acción**: Crea una fucnión llamada `agrega_iva`, a la cual reciba un valor numérico, a le agregue el 16% de IVA:

Ejemplo de uso:
```python
precio = 100
precio_iva = agrega_iva(precio)
print(precio_va) # 116
```

2.-  ¡Bien! Después de haber creado tu función, te comentan que abrieron una sucursal en Tijauana, y que allá el IVA no es 16%, como ocurre en zonas de la frontera norte. Ahora la empresa necesita configurar ese valor.

**Acción**: Agrega un argumento llamado `tasa_iva`, cuyo valor por defecto sea 16.

```python
print(agrega_iva(100, tasa_iva=8))  # 108
```

3.- Han pasado los meses, y la empresa factura cada vez mas productos. Un colega te comenta que sería mas sencillo que la función calcule el IVA de varios productos, no sólo de uno. El detalle está en que no sabemos con anticipación cuantos productos llegarán.

**Acción**: Utiliza *args para calcular el IVA de varios productos. Regresa el total de la suma de productos, junto con el IVA a la tasa indicada.

```python
ptrint(agrega_iva(50, 50, tasa_iva=15))  # 115
```

4.- **Reto extra**: Después de una reforma fiscal, ahora ciertos productos que vende Don Panchito, ya no generan IVA. Tus colegas comentan que la información viene en un diccionario como el siguiente:
```python
{
	"precios": [100, 50, 30],
	"exento_iva": False, False, True
}
```

¿Cómo cambiarías la función para que aceptes este tipo de argumentos?


<details>
	Ejercicio 1 
	def reto1(operacion, *args):
		resultado = 0
		if operacion == '*':
			resultado = 1
		for arg in args:
			if operacion == '+':
				resultado += arg
			elif operacion == '*':
				resultado *= arg
		return resultado

	suma = reto1('+',2,3,4)
	multiplicacion = reto1('*',1,3,4)
	print(suma)
	print(multiplicacion)


	Ejercicio 2 
	def directorio1(**kwargs):
		ordenado = sorted(kwargs)
		for dato in ordenado:
			print(dato, kwargs[dato])    


	directorio1(Richie='12345', Daniela = '0987')


</details> 



