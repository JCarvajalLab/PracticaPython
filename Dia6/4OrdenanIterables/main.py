#  Funciona por que no es tupla
#  estudiantes = ["Juan","Jose","Pedro","Alex","Milagros"]

# estudiantes.sort()
# for i in estudiantes:
#     print(i)

#Se ordena alfabeticamente en una tupla
# estudiantes = ("Juan","Jose","Pedro","Alex","Milagros")

# estudiantes2 = sorted(estudiantes)
# for i in estudiantes2:
#     print(i)

#Se ordenta desde la Z a la A

estudiantes = ("Juan","Jose","Pedro","Alex","Milagros")

estudiantes2 = sorted(estudiantes, reverse=True)
for i in estudiantes2:
    print(i)