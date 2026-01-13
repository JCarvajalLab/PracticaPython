class Animal:
    def comer(self):
        print("Este animal esta comiendo")

class Conejo(Animal):
    def comer(self):
        print("Este conejo fue comido")

conejo = Conejo()
print(conejo.comer())