from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def ir(self):
        pass

class Coche(Vehiculo):
    def ir(self):
        print("Conduces el auto")
    def detener(self):
        print("EEste coche esta detenido")

class Motocicleta(Vehiculo):
    def ir(self):
        print("Andas en moto")
    def detener(self):
        print("Esta moto esta detenido")

# vehiculo = Vehiculo()
coche = Coche()
motocicleta = Motocicleta()

# vehiculo.ir()
coche.ir()
motocicleta.ir()