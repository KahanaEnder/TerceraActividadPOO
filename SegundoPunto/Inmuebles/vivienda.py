from Inmuebles import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones:int, num_banos:int):
        super().__init__(id_inmobiliario, direccion, area)
        self._num_habitaciones = num_habitaciones
        self._num_banos = num_banos

    def imprimir(self):
        print(f"Numero de habitaciones: {self._num_habitaciones}")
        print(f"Numero de baños: {self._num_banos}")
        super().imprimir()