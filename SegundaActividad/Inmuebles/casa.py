from .vivienda import InmuebleVivienda

class Casa(InmuebleVivienda):
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos:int):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos)
        self._pisos = pisos

    def imprimir(self):
        print(f"Pisos: {self._pisos}")
        super().imprimir()


class CasaRural(Casa):
    _valorArea:float = 1500000 #Protected static float
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos, distancia_cabecera:int, altitud:int):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def imprimir(self):
        print(f"Distancia cabecera: {self._distancia_cabecera}")
        print(f"Altitud: {self._altitud}")
        super().imprimir()


class CasaUrbana(Casa):
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos)
    
    def imprimir(self):
        super().imprimir()

class CasaConjuntoCerrado(CasaUrbana):
    _valorArea = 2500000
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos,valorAdmin:int,tienePiscina:bool,tieneCamposDeportivos:bool):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos)
        self._valorAdmin = valorAdmin
        self._tienePiscina = tienePiscina
        self._tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        print(f"Valor de administración: {self._valorAdmin}")
        print(f"Tiene piscina: {self._tienePiscina}")
        print(f"Tiene campos deportivos: {self._tieneCamposDeportivos}")
        super().imprimir()
    
class CasaIndependiente(CasaUrbana):
    _valorArea:float = 3000000
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos, pisos)

    def imprimir(self):
        super().imprimir()