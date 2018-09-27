# Miriam Grizel González Sandoval
# 214691138

while True:
    question = str(input('Quiere salir? s/n '))
    if question.lower() == 's':
        break
    else:
        grades = int(input('Temperatura del cultivo:'))
        if grades < 40:
            print('Todo bien!')
        else:
            print('Tu cultvo esta en peligro!')
