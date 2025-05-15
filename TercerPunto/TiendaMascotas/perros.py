from TiendaMascotas import Mascota
class Perros(Mascota):
    def __init__(self, nombre, edad, color,peso:int,muerde:bool):
        super().__init__(nombre, edad, color)
        self._peso:int = peso
        self._muerde:bool = muerde
    #metodo estatico, no necesita self, puede o no recibir parametros de instancia pero es propio de la clase
    @staticmethod
    def sonido():
        print("Los perros ladran")

class PerroGrande(Perros):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class PerroMediano(Perros):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class PerroPequeno(Perros):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)

class Caniche(PerroPequeno):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class YorkshireTerrier(PerroPequeno):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Schnauzer(PerroPequeno):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Chihuahua(PerroPequeno):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)

class Collie(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Dalmata(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Bulldog(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Galgo(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Sabueso(PerroMediano):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)

class PastorAleman(PerroGrande):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Doberman(PerroGrande):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)
class Rotweiller(PerroGrande):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color, peso, muerde)