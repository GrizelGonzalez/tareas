from random import choice

opctions = ['piedra', 'papel', 'tijera']
maquina = choice(opctions)

while True:
    print('''
1.- piedra
2.- papel
3.- tijera 
''')
    jugador = int(input())

    if jugador == 1:
        jugador = 'piedra'
    elif jugador == 2:
        jugador = 'papel'
    elif jugador == 3:
        jugador = 'tijera'

    print('Jugador:', jugador)
    print('Maquina:', maquina)

    if jugador == maquina:
        print('¡Empate!')
    elif jugador == 'piedra' and maquina == 'papel' or jugador == 'tijera' and maquina == 'piedra' \
            or jugador == 'papel' and maquina == 'tijera':
        print('¡Perdiste!')
    else:
        print('¡Ganaste!')

    re_ask = input('¿Quieres seguir jugando? "S/N" ')
    if re_ask.lower() != 's':
        break
