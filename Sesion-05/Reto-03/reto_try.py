def promedio(num1,num2):
    try:
        return  (num1+num2)/2
    except NameError:
        print("Datos nos validos")
        return 0
    except TypeError:
        print("Datos no validos")
        return 0
    except:
        print("ocurrió un error")
        return 0
    


print(promedio(3,'a'))
print(promedio(2,3))