def saludo(pNombre, apellido, edad):
    print("Hola " + pNombre + " " + apellido)
    print("Tienes " + str(edad) + " Anos")
    print("Que tengas un buen dia!")

# nombre = "jose"
nombre = input("Ingresa tu nombre ")

saludo(nombre, "Smith", 24)