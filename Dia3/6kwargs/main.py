##empaqueta los argumentos en un diccionario

def hola(**kwargs):
    # print('hola ' + kwargs['nombre'] + ' ' + kwargs['apellido'] + ' ' + kwargs['segundoNombre'])
    print('hola', end=' ')
    for clave,valor in kwargs.items():
        print(valor, end=' ')

hola(titulo='Senor', nombre='jose', apellido='ulloa', segundoNombre='python')