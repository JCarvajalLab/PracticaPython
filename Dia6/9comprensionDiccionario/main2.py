#diccionario = {key: expresion for (key, value) in iterable if condicion}

clima = {'New York':'Nieve', 'Boston':'Soleado', 'Los Angeles':'Soleado', 'Chicago':"Nunlado"}

climaSoleado = {key: value for (key,value) in clima.items() if value == 'Soleado'}
print(climaSoleado)