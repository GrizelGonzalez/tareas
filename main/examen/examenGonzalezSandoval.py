from random import randint

alazar = randint(1, 100)
numerointentos = 9
flag = True

while flag:
    player = int(input('Escribe un numero  de 1 al 100: '))

    if 1 <= player <= 100:
        if numerointentos > 0:

            if player == alazar:
                print('Felicidades ganaste!!!')
                opc = input('Quieres continuar jugando s/n: ')
                if opc.lower() != 's':
                    flag = False

            if player < alazar:
                print('Te falta!')
                print('Numero de intentos:', numerointentos + 1)
                numerointentos -= 1

            if player > alazar:
                print('Te has pasado')
                print('Numeros de intentos:', numerointentos + 1)
                numerointentos -= 1

        else:
            print('Se han terminado tus intentos')
            flag = False
    else:
        print('Estas fuera del rango!')
