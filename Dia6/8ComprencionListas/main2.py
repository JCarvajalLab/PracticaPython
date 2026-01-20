# estudiantes = [100,90,80,70,60,50,40,30,0]

# estudiantesAprobados = list(filter(lambda x: x >= 60, estudiantes))
# print(estudiantesAprobados)

estudiantes = [100,90,80,70,60,50,40,30,0]
estudiantesAprobados = [ i for i in estudiantes if i >= 60 ]
#estudiantesAprobados = [ i if i >= 60 else '-' for i in estudiantes]
print(estudiantesAprobados)