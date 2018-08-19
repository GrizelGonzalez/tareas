#name = input("Ingresa tu nombre: ")
#year = int(input("Ingresa tu edad: "))
#height = float(input("Ingresa tu altura: "))
#print("Nombre: "+name+", Edad: "+str(year)+", Altura: "+str(height))

""" Esto es un dicionario o lista de datos donde se conforma por una clave y en un valor por ejemplo = 'clave':"valor"
en este caso el valor es el dato que pongas en el input() """

Input = {'Nombre': input('Ingresa tu nombre: '), 'Edad': input('Ingresa tu edad: '), 'Altura': input('Ingresa tu altura: ')}

'''El for se repetira la veces que tiene una clave en caso 3'''

for key in Input:
    '''Al final solo va imprimiendo el dicionario con su clave y valor según como a avance el for, que serán 3 veces,
        end='' solo quita el salto de linea al print y le puse una coma y un espacio'''
    print(key+': '+Input[key], end=", ")

'''Nota: Arriba esta tu tarea normal un poquito mejorada y te deje esa otra...todo es diferente a la mía y
         mejor que la mía diría yo tu decides que usar queda a tu opinión'''