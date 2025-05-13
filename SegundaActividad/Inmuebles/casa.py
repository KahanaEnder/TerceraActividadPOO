from .vivienda import Vivienda

class Casa(Vivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self._pisos = pisos


class CasaRural(Casa):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos, distancia_cabecera, altitud):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def calcular_valor_compra(self):
        return self._area * 1500000


class CasaUrbana(Casa):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos, conjunto_cerrado, valor_admin=0, incluye_comunes=False):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos, pisos)
        self._conjunto_cerrado = conjunto_cerrado
        self._valor_admin = valor_admin
        self._incluye_comunes = incluye_comunes

    def calcular_valor_compra(self):
        if self._conjunto_cerrado:
            return self._area * 2500000
        else:
            return self._area * 3000000
