temperatura = int(input("Cual es la temperatura de afuera? "))

if (temperatura >= 0 and temperatura <= 30):
    print("La temperatura esta agradable, sal con tranquilidad")
elif (temperatura < 0 or temperatura > 30):
    print("La temperatura esta mal hoy. quedate adentro te vas a cagar de calor o de frio")

##Si le agregamos el not cambia la condicion cambia el verdadero en falso

# temperatura = int(input("Cual es la temperatura de afuera? "))

# if not (temperatura >= 0 and temperatura <= 30):
#     print("La temperatura esta agradable, sal con tranquilidad")
# elif not (temperatura < 0 or temperatura > 30):
#     print("La temperatura esta mal hoy. quedate adentro te vas a cagar de calor o de frio")