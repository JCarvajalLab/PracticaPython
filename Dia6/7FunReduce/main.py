import functools

letras = ["H","O","L","A"]
# Ejemplo de como funciona
# letras = ["H","O","L","A"]
# letras = ["HO","L","A"]
# letras = ["HOL","A"]
# letras = ["HOLA"]

palabra = functools.reduce(lambda x,y: x+y, letras)
print(palabra)