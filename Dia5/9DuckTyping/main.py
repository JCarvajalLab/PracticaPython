class Pato:
    def caminar(self):
        print("Este pato esta caminando")
    def hablar(self):
        print("Este pato esta haciendo cuak")

class Gallina:
    def caminar(self):
        print("Esta gallina esta caminando")
    def hablar(self):
        print("Esta gallina esta cacareando")

class Persona:
    def atrapar(self, pato):
        pato.caminar()
        pato.hablar()
        print("!Lo Atrapaste!")

pato = Pato()
gallina = Gallina()
persona = Persona()

persona.atrapar(pato)
persona.atrapar(gallina)

# Solo funciona si tienen los mismos atributos y metodos