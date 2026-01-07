try:
    with open('1LeerArchivos/block.txt') as file: ## No funciona solo con el block.txt por que en este momento estoy desde la carpeta dia4 y no desde 1leerarchivos
        print(file.read())

except FileNotFoundError:
    print("El archivo no fue encontrado")