import random

precio = int(random.randint(1, 500))
articulo = input("Nombre del articulo: ")
print("Precio de "+articulo+" es $"+precio)

flag = True
while flag:
    pago = int(input("Ingrese su pago: "))
    if pago < precio:
        print("Dinero insufisiente!")
        flag = True
    else:
        print("Total:{precio}")
        print("Pago:{pago}")
        print("Cambio: {pago-precio}")
        flag = False

