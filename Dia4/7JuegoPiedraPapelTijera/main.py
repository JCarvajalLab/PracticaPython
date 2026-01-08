import random

lista = ['piedra', 'papel', 'tijera']

computadora = random.choice(lista)
jugador = None

while jugador not in lista:
    jugador = input(" Piedra, Papel o Tijeras: ").lower()
    if jugador == computadora:
        print('Computadora: ', computadora)
        print('Jugador: ', jugador)
        print('Empate')
    elif jugador == 'piedra':
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste')
        if computadora == 'tijeras':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste')
    elif jugador == 'papel':
        if computadora == 'tijera':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste')
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste')
    elif jugador == 'tijera':
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste')
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste')

    jugarDenuevo = input("Quieres volver a jugar: (si/no)").lower()

    if jugarDenuevo != 'si':
        break
print("Chao qliao")