from .inmueble import Inmueble

class Vivienda(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_banos):
        super().__init__(id_inmobiliario, area, direccion)
        self._num_habitaciones = num_habitaciones
        self._num_banos = num_banos
