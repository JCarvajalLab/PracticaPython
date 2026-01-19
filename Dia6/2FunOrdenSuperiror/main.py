def hablarAlto(texto):
    return texto.upper()
def hablarBajo(texto):
    return texto.lower()
def hola(func):
    texto = func("Hola ")
    print(texto)

hola(hablarAlto)
hola(hablarBajo)