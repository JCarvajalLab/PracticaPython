##Eliminar un archivo
import os

path = ('5EliminarArchivos\\hola.txt')
try:
    os.remove(path)
except FileNotFoundError:
    print("El archivo no fue encontrado")
# except PermissionError:
#     print("No tienes permiso para elimiar esta carpeta") Esto se utiliza cuando se intenta eliminar una carpeta


#Eliminar una carpeta vacia
import os

path = ('5EliminarArchivos\\carpeta')
try:
    os.rmdir(path)
except FileNotFoundError:
    print("El archivo no fue encontrado")
except PermissionError:
    print("No tienes permiso para elimiar esta carpeta")
else:
    print(path + " Fue eliminado")

#Eliminar una carpeta con archivos adentro

import os
import shutil

path = ('5EliminarArchivos\\carpeta')
try:
    shutil.rmtree(path)
except FileNotFoundError:
    print("El archivo no fue encontrado")
except PermissionError:
    print("No tienes permiso para elimiar esta carpeta")
except OSError:
    print("No puedes eliminar esta carpeta")
else:
    print(path + " Fue eliminado")