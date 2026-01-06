##empaqueta los argumentos en una tupla

def suma(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

print(suma(9, 5, 6))