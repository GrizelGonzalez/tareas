lista = ["Ana", "Luis", "Pedro", "Juan"]
while True:
    print(lista)
    remover = input('Escribe el nombre que desea remover: ')
    lista.remove(remover.capitalize())
    nombre = input("Ingrese el nombre nuevo para agregar: ")
    lista.append(nombre.capitalize())
    print(lista)

    opc = input('¿Desea continuar? s/n: ')
    if opc.lower() != 's':
        break

