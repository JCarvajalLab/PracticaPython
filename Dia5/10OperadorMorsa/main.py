# feliz = True
# print(feliz)
# es lo mismo
# print(feliz := True)

# comidas = []
# while True:
#     comida = input("Que comida te gusta? ")
#     if comida == "salir":
#         break
#     comidas.append(comida)


comidas = []
while (comida := input("Que comida te gusta? ")) != "salir":
    comidas.append(comida)