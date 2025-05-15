from TiendaMascotas import Mascota
class Gatos(Mascota):
    def __init__(self, nombre, edad, color,alturaSalto:float,longitudSalto:float):
        super().__init__(nombre, edad, color)
        self._alturaSalto:float = alturaSalto
        self._longitudSalto:float = longitudSalto
    @staticmethod
    def sonido():
        print("Los gatos maullan y ronronean")

class GatoSinPelo(Gatos):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class GatoPeloLargo(Gatos):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class GatoPeloCorto(Gatos):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)

class Esfinge(GatoSinPelo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Elfo(GatoSinPelo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Donskoy(GatoSinPelo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)

class Angora(GatoPeloLargo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Himalayo(GatoPeloLargo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Balines(GatoPeloLargo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Somali(GatoPeloLargo):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)

class AzulRuso(GatoPeloCorto):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Britanico(GatoPeloCorto):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class Manx(GatoPeloCorto):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
class DevonRex(GatoPeloCorto):
    def __init__(self, nombre, edad, color, alturaSalto, longitudSalto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)