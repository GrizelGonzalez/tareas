Input = {'Nombre': input('Ingresa tu nombre: '), 'Edad': input('Ingresa tu edad: '), 'Altura': input('Ingresa tu altura: ')}
for key in Input:
    print(key+': '+Input[key], end=", ")