from .vivienda import Vivienda

class Apartamento(Vivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos, valor_admin):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_banos)
        self._valor_admin = valor_admin


class Apartaestudio(Apartamento):
    def __init__(self, id_inmobiliario, area, direccion, valor_admin):
        super().__init__(id_inmobiliario, area, direccion, 1, 1, valor_admin)

    def calcular_valor_compra(self):
        return self._area * 1500000


class ApartamentoFamiliar(Apartamento):
    def calcular_valor_compra(self):
        return self._area * 2000000
