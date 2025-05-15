from Inmuebles import InmuebleVivienda

class Apartamento(InmuebleVivienda):
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos):
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos)

    def imprimir(self):
        super().imprimir()


class Apartaestudio(Apartamento):
    _valorArea:float = 1500000
    def __init__(self, id_inmobiliario, direccion, area):
        super().__init__(id_inmobiliario, direccion, area, 1, 1, ) #num_habitaciones y num_banos no es configurable asi

    def imprimir(self):
        super().imprimir()




class ApartamentoFamiliar(Apartamento):
    _valorArea:float = 1500000
    def __init__(self, id_inmobiliario, direccion, area, num_habitaciones, num_banos,valorAdmin):
        self._valorAdmin = valorAdmin
        super().__init__(id_inmobiliario, direccion, area, num_habitaciones, num_banos)

    def imprimir(self):
        print(f"Valor de administración: {self._valorAdmin}")
        super().imprimir()
