#Miriam Grizel González Sandoval
#214691138
lista = [int(input("Ingrese valor 1: ")),
         int(input("Ingrese valor 2: ")),
         int(input("Ingrese valor 3: "))]

inc = 1
for inc in range(1, len(lista), inc*3+1):
    while inc > 0:
        for i in range(int(inc), len(lista)):
            j = i
            temp = lista[i]
            while j >= int(inc) and lista[j-int(inc)] > temp:
                lista[j] = lista[j-inc]
                j = j-inc
            lista[j] = temp
        inc = inc/2

print("\nValores ya ordenados:", str(lista).strip('[]'))
