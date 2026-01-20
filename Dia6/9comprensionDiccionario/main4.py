#diccionario = {key: function(value) for (key, value) in iterable}

def checkTemp(value):
    if value >= 70:
        return "Calor"
    elif 60>= value >=40:
        return "Normal"
    else:
        return "Frio"

ciudades = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
clima = {key: checkTemp(value) for (key,value) in ciudades.items()}
print(clima)