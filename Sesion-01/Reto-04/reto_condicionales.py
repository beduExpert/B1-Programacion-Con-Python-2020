print("Qué topping quieres en tu helado?")
topping = input()

if topping == "oreo":
    precio = 19
elif topping == "m&m":
    precio = 25
elif topping == "fresas":
    precio = 22
elif topping  == "brownie":
    precio = 28
else:
    print("producto no disponible")

print("El precio es ${}".format(precio))

