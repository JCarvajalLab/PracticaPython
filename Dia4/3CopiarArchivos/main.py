# copyfile() copia el contenido de un archivo a otro 
# copy() Todo lo de el copyfile y tambien copia los permisos y el destino puede ser un directorio
# copy2() todo lo de copy y tambien copia metodos, fecha de creacion y modificacion  

import shutil

shutil.copyfile('3CopiarArchivos/test.txt', '3CopiarArchivos\\copy.txt') #El primero es el origen y el segundo es el destino de donde se va a copiar
shutil.copy('3CopiarArchivos/test.txt', '3CopiarArchivos\\copy.txt')
shutil.copy2('3CopiarArchivos/test.txt', '3CopiarArchivos\\copy.txt')