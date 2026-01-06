# while 1==1:
#     print("ayuda! Estoy atrapado")

## si el bucle no se cancela continua hasta que uno fuerze la cancelacion

##Opcion 1
# nombre = ""

# while len(nombre) == 0:
#     nombre = input("Ingresa tu nombre: ")

##opcion 2 
nombre = ""

while not nombre or len(nombre) == 0:
    nombre = input("Ingresa tu nombre: ")
print("Hola " + nombre)