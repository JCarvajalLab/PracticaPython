class Animal:
    vivo = True

    def comer(self):
        print("Esta Comiendo!")

    def dormir(self):
        print("Esta Durmiendo!")

class Conejo(Animal):
    def correr(self):
        print("Corriendo")

class Pez(Animal):
    def nadar(self):
        print("Nadando")

class Halcon(Animal):
    def volar(self):
        print("Volando")

conejo = Conejo()
pez = Pez()
halcon = Halcon()

halcon.volar()