#diccionario = {key: expresion for (key, value) in iterable}

ciudadesEnF = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}

ciudadesEnC = {key:round((value-32)*(5/9)) for(key, value) in ciudadesEnF.items()}

print(ciudadesEnC)