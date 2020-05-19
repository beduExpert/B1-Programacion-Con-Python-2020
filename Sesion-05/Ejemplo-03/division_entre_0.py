a = 4
b = 0
#Si ocurre un error durante la ejecución de el try, se ejecuta el except
try:
    c = a/b
    print ("El resultado de la división es {}".format(c))
except:
    print("No puedes dividir entre 0")

#Se pueden definir distintas medidas a tomar para distinto tipo de error
try:
    c = a/x
except NameError:
    print("Alguna variable no fue definida")
except ZeroDivisionError:
    print("No puedes dividir entre 0")
except: #Si se cae en un error no definido anteriormente
    print("Ocurrió otro error")
