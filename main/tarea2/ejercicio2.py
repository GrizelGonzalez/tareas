import random

precio = int(random.randint(1, 500))
articulo = input("Nombre del articulo: ")
print("Precio de "+articulo+" es $"+str(precio))

flag = True
while flag:
    pago = int(input("Ingrese su pago: "))
    if pago < precio:
        print("Dinero insufisiente!")
        flag = True
    else:
        print("Total:"+str(precio))
        print("Pago:"+str(pago))
        print("Cambio:"+str(pago-precio))
        flag = False

