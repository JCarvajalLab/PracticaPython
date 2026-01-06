nombre = 'jose peralta'

# if nombre[1].islower():
#     nombre = nombre.capitalize() ##transformamos un elemento que se encuentre en minuscula a mayuscula

primerNombre = nombre [:4].upper() ##seleccionamos solo el nombre y lo convertimos con el upper a mayusculas
primerApellido = nombre[5:].lower()
ultimoCaracter = nombre[-2]

print(ultimoCaracter)