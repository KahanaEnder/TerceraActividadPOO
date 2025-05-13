from .inmueble import Inmueble

class Local(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, localizacion):
        super().__init__(id_inmobiliario, area, direccion)
        self._localizacion = localizacion


class LocalComercial(Local):
    def __init__(self, id_inmobiliario, area, direccion, localizacion, centro_comercial):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self._centro_comercial = centro_comercial

    def calcular_valor_compra(self):
        return self._area * 3000000


class Oficina(Local):
    def __init__(self, id_inmobiliario, area, direccion, localizacion, es_gobierno):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self._es_gobierno = es_gobierno

    def calcular_valor_compra(self):
        return self._area * 3500000
