from enum import Enum
from Inmuebles import Inmueble

class Local(Inmueble):
    class Tipo(Enum):
        INTERNO = "INTERNO"
        CALLE = "CALLE"
    def __init__(self, id_inmobiliario, direccion, area,tipoLocal:Tipo):
        super().__init__(id_inmobiliario, direccion, area)
        self._tipoLocal = tipoLocal
    
    def imprimir(self):
        print(f"Tipo de local: {self._tipoLocal}")
        return super().imprimir()


class LocalComercial(Local):
    _valorArea:float = 3000000
    def __init__(self, id_inmobiliario, direccion, area, tipoLocal,centroComercial):
        super().__init__(id_inmobiliario, direccion, area, tipoLocal)
        self._centroComercial = centroComercial

    def imprimir(self):
        print(f"Centro comercial: {self._centroComercial}")
        return super().imprimir()


class Oficina(Local):
    _valorArea:float = 3500000
    def __init__(self, id_inmobiliario, direccion, area, tipoLocal,esGobierno:bool):
        super().__init__(id_inmobiliario, direccion, area, tipoLocal)
        self._esGobierno = esGobierno

    def imprimir(self):
        print(f"Es oficina gubernamental: {self._esGobierno}")
        return super().imprimir()
