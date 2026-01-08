import os

origen = '4moverArchivos\\hola.txt' 
destino = 'C:\\Users\\NombreComputador\\Desktop\\hola.txt'

try:
    if os.path.exists(destino):
        print("Existe un archivo en este destino")
    else:
        os.replace(origen, destino)
        print(origen + " Archivo fue trasladado")
except FileNotFoundError:
    print(origen + " No se encontro el archivo")