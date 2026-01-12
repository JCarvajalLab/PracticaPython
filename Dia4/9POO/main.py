from automovil import Auto

auto1 = Auto("Chevy", "Corvette", 2023, "Azul")
auto2 = Auto("Ford", "Mustang", 2022, "Rojo")

print(auto1.marca)
print(auto1.modelo)
print(auto1.ano)
print(auto1.color)

auto1.encendido()
auto1.apagado()