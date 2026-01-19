tienda = [("Camisa", 20.00),
            ("Pantalones", 25.00),
            ("Chaqueta", 50.00),
            ("Medias", 10.00)]

funEuro = lambda datos:(datos[0], datos[1]*0.96)
funDolar = lambda datos:(datos[0], datos[1]/0.96)

tienda2 = list(map(funEuro, tienda))
for i in tienda2:
    print(i)

tienda2 = list(map(funDolar, tienda))
for i in tienda2:
    print(i)