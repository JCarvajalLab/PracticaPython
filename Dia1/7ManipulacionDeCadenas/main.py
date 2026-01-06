nombre = "Alex Silva"
primer_nombre = nombre [0:4] ## se puede escribir tambien [:4]
apellido = nombre [5:10] ## se puede escribir tambien [:10]

nombre_dos = nombre[0:10:1] ## se puede escribir tambien [::1]

nombre_invertido = nombre[::-1] ## cadena invertida (el nombre al reves)


## opcion 1##################################################################################
website = "http://www.google.com"

slice = slice(11,17) ## tambien puede ser asi slice(11, -4) el -4 es desde el final hacia atras 
print(website[slice])

## opcion 2##################################################################################
website = "http://www.wikipedia.com"

slice = slice(11,-4)
sitio = website[slice]

print(sitio)