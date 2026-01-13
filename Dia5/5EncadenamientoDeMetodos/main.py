class Coche():
    def encender(self):
        print("El Vehiculo a encendido el motor")   
        return self
    def conducir(self):
        print("Estas conduciendo el vehiculo")
        return self
    def frenar(self):
        print("Estas pisando los frenos")
        return self
    def apagar(self):
        print("Estas apagando el motor")
        return self

coche = Coche()


coche.encender().conducir().frenar().apagar()
coche.encender()\
        .conducir()\
        .frenar()\
        .apagar()
