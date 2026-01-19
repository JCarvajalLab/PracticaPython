# estudiantes = [("Juan", "F", 60),
#                 ("Jose", "A", 24),
#                 ("Pedro", "D", 33),
#                 ("Alex", "B", 19),
#                 ("Milagros", "C", 43)]

# #Ordenar por nombre
# estudiantes.sort()

# for i in estudiantes:
#     print(i)

# #Odenar por calificacion
# calificacion = lambda tupla: tupla[1]
# estudiantes.sort(key=calificacion)

# for i in estudiantes:
#     print(i)

# #ordenar por edad 

# edad = lambda tupla: tupla[2]
# estudiantes.sort(key=edad)

# for i in estudiantes:
#     print(i)

##Tupla de una tupla 

estudiantes = (("Juan", "F", 60),
                ("Jose", "A", 24),
                ("Pedro", "D", 33),
                ("Alex", "B", 19),
                ("Milagros", "C", 43))

edad = lambda tupla: tupla[2]
estudiantes2 = sorted(estudiantes, key=edad)

for i in estudiantes2:
    print(i)