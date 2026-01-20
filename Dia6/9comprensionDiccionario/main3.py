#diccionario = {key: (if/else) for (key, value) in iterable}

clima = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
clima2 = {key: ("Calor" if value >= 40 else "Frio") for (key,value) in clima.items()}
print(clima2)