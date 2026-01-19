amigos = [("Laura", 22 ),
            ("Juan", 19),
            ("Laura", 25),
            ("Sofia", 17),
            ("Carlos", 20),
            ("Maria", 16),
]

edad = lambda dato:dato[1] >= 18
amigosBebedores = list(filter(edad, amigos))

for i in amigosBebedores:
    print(i)