capitales = {
    'francia':'paris',
    'argentina': 'buenos aires',
    'chile': 'santiago',
    'brazil': 'brasilia',
    'cursos' :['python', 'c#']
}

capitales.update({'alemania': 'berlin'})
# capitales.pop('chile') ##elimina un elemento del diccionario
# capitales.clear() ##limpiamos todo el diccionario



# print(capitales.get('chile'))
# print(capitales.keys())
# print(capitales.values())
#print(capitales.items())

for key, value in capitales.items():
    print(key, value)