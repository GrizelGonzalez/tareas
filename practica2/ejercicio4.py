from random import randint


def suma(valor1, valor2):
    return print(valor1 + valor2)


def random(valor1, valor2):
    return print(randint(valor1, valor2))


def ecuacion(valor1, valor2):
    x = 0
    if valor1 != 0:
        x = valor2 / valor1
    else:
        if valor2 != 0:
            print('No es posible la solucion')
        else:
            print('Indefinido')
    return print(x)


def menu():
    valor1 = float(input('Ingrese valor 1: '))
    valor2 = float(input('Ingrese valor 2:'))
    print("""
    1.- Suma
    2.- Random valor
    3.- Ecuacion de primer grado
    """)
    while True:
        opc = int(input())
        if opc == 1:
            suma(valor1, valor2)
            break
        elif opc == 2:
            random(valor1, valor2)
            break
        elif opc == 3:
            ecuacion(valor1, valor2)
            break
        else:
            print('Solucion incorrecta')
            print('Seleccionar otra vez: ')


menu()
