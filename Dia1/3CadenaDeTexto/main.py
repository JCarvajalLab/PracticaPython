nombre = "alexander"

print(len(nombre))
#Len se utiliza para saber la cantidad de caracteres

print(nombre.find("l"))
#Se utiliza para saber la posicion de un caracter

print(nombre.capitalize())
#transforma la primera letra a mayuscula

print(nombre.upper())
#transforma todas las letra a mayusculas

print(nombre.lower())
#transforma todas las letra a minusculas

print(nombre.isdigit())
#detecta si es numero con un true o false si no lo es

print(nombre.isalpha())
#Para validar si hay espacio o caracter especial en nuestra cadena de texto

print(nombre.count("e"))
#nos muestra la cantidad de letras que se repiten en la cadena, no cuentan la mayusculas

print(nombre.replace("x" , "o"))
#Reemplaza una letra por otra

print(nombre*4)
#mostrar una cadena varias veces