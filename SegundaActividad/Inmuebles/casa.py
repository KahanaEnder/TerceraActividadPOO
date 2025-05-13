from vivienda import InmuebleVivienda

class Casa(InmuebleVivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos:int):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self._pisos = pisos

    def imprimir(self):
        print(f"Pisos: {self._pisos}")
        return super().imprimir()


class CasaRural(Casa):
    _valorArea:float = 1500000 #Protected static float
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos, distancia_cabecera:int, altitud:int):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def imprimir(self):
        print(f"Distancia cabecera: {self._distancia_cabecera}")
        print(f"Altitud: {self._altitud}")
        return super().imprimir()


class CasaUrbana(Casa):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos)

