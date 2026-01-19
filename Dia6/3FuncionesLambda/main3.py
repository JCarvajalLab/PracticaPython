doble = lambda x: x * 2 
multiplicar = lambda x, y: x * y
suma = lambda x,y,z: x + y +z
nombreCompleto = lambda nombre, apellido: nombre + " " + apellido
checkEdad = lambda edad: True if edad >= 18 else False

print(suma(5,6,7))
print(nombreCompleto("Alex", "Sanchez"))
print(checkEdad(19))

#definir funciones en una sola linea en python