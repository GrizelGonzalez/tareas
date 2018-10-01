lista = ["Ana", "Luis", "Pedro", "Juan"]
while True:
    print(lista)
    nombre = input("Ingrese el nombre a eliminar : ")
    lista.remove(nombre.capitalize())
    print(lista)

    opc = input('¿Desea continuar? s/n: ')
    if opc.lower() != 's':
        break
