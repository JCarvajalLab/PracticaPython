import os

path = 'C:\\Users\\Deo\\Desktop\\BOOTCAMP\\git comandos basicos.txt'

if os.path.exists(path):
    print('Existe')
    if os.path.isfile(path):
        print('Es un archivo')
else:
    print('No existe')