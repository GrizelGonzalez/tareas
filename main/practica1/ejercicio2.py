numero = int(input("Digite tabla a calcular: "))

try:
    numero = int(numero)
except ValueError:
    print("Debe ingresar un número, repita el procedimiento")
    import sys
    sys.exit()


contador = 1
while contador < 11:
    print(str(contador) + " x " + str(numero) + " = " + str(contador * numero))
    print
    contador+=1