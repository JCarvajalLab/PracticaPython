## Opcion 1 de importacion
import mensaje as msg

msg.hola()
msg.adios()

## Opcion 2 de importacion
from mensaje import hola, adios

hola()
adios()

## Opcion 3 de importacion, no recomendable en proyectos grandes
from mensaje import *

hola()
adios()