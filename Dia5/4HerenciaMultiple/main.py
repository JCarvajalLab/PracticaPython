class Presa():
    def huir(self):
        print("Este animal huye")

class Depredador():
    def cazar(self):
        print("Este Animal esta cazando")

class Conejo(Presa):
    pass

class Halcon(Depredador):
    pass

class Pez(Presa, Depredador):
    pass

conejo = Conejo()
halcon = Halcon()
pez = Pez()

# conejo.huir()
# halcon.cazar()
pez.cazar()
pez.huir()