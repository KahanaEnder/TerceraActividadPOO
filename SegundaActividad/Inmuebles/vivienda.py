from inmueble import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones:int, num_banos:int):
        super().__init__(id_inmobiliario, area, direccion)
        self._num_habitaciones = num_habitaciones
        self._num_banos = num_banos

    def imprimir(self):
        print(f"Numero de habitaciones: {self._num_habitaciones}")
        print(f"Numero de baños: {self._num_banos}")
        return super().imprimir()