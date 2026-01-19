class Coche:
    color = None
class Motocicleta:
    color = None

def cambiarColor(vehiculo, color):
    vehiculo.color = color

coche1 =Coche()
coche2 =Coche()
coche3 =Coche()
motocicleta = Motocicleta()

cambiarColor(coche1, 'Rojo')
cambiarColor(coche2, 'Azul')
cambiarColor(coche3, 'Amarillo')
cambiarColor(motocicleta, 'verde')

print(coche1.color)
print(coche2.color)
print(coche3.color)

print(motocicleta.color)
