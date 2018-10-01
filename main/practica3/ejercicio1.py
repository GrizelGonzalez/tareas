lista = []

opc = 'y'
while opc == 'y':
    valor = float (input("Dame un valor"))
    lista.append(valor)
    print("¿Otro valor?")
    opc = input("s = si/n = no")
print(lista)
sum = 0.0
suma2 = 0.0

for i in range(0, len(lista)):
    sum = sum+lista[i]
    media = sum/len(lista)
    print("La media es:", media)
    print("La suma de la lista es: ", sum)

