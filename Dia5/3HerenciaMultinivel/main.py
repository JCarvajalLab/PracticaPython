class Organimos:
    vivo = True

class Animal(Organimos):
    def comer(self):
        print("ESTE ANIMAL ESTA COMIENDO")

class Perro(Animal):
    def ladrar(self):
        print("ESTE PERRRO ESTA LADRANDO!!")


perro = Perro()

print(perro.vivo)

print(perro.comer())

print(perro.ladrar())