import random

x = random.randint(1, 6)
y = random.random()

mi_lista = ['piedra', 'papel', 'tijeras']
z = random.choice(mi_lista) ## elegir al azar


cartas = ['1','2','3','4','5','6','7','8','9','J','Q','K','A']
random.shuffle(cartas) ## mesclar las cartas

print(cartas)