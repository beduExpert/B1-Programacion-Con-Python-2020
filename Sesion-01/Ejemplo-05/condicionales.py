# If sirve para establecer una condición que de cumplirse ejecutará cierto código
edad  = 25
if edad > 18:
    print ("La persona es mayor de edad")

#El código dentro de else se ejecutará cuando no se cumpla la condición entablecida en el if

velocidad = 70
limite = 90

if velocidad > limite:
    print("Excedes el límite de velocidad")
else:
    print("Vas a una velocidad adecuada")
    
# En caso de tener varias opciones se puede usar Elif

numero = 7

if numero == 0:
    print("El número es 0")
elif numero > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

