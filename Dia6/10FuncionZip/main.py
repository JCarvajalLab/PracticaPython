# nombreUsuario = ["Alex", "Sanchez","Pedro"]
# contrasena = ("123","abc","contrasena")

# usuarios = list(zip(nombreUsuario, contrasena))

# for i in usuarios:
#     print(i)
#################################################################### solo 2 elementos
# nombreUsuario = ["Alex", "Sanchez","Pedro"]
# contrasena = ("123","abc","contrasena")

# usuarios = dict(zip(nombreUsuario, contrasena))

# for key,value in usuarios.items():
#     print(key + ' : ' + value)

#################################################################### agrega elemento de 2 o mas iterables de distintos tipos
nombreUsuario = ["Alex", "Sanchez","Pedro"]
contrasena = ("123","abc","contrasena")
FechaSesion = ["01/04/2026", "12/12/2026","06/06/2026"]

usuarios = list(zip(nombreUsuario, contrasena, FechaSesion))

for i in usuarios:
    print(i)