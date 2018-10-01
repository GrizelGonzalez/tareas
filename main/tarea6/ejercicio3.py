from random import randint

lista_matriz = []
fila = 0

while fila < 3:
    fila += 1
    lista_matriz.append([])

    columna = 0
    while columna < 4:
        columna += 1
        num = randint(0, 100)
        lista_matriz[fila-1].append(num)

    print(lista_matriz[fila-1])


