from .inmueble import Inmueble
from .vivienda import InmuebleVivienda
from .casa import Casa, CasaRural, CasaUrbana
from .apartamento import Apartamento, Apartaestudio, ApartamentoFamiliar
from .local import Local, LocalComercial, Oficina

__all__ = [
    "Inmueble", "InmuebleVivienda",
    "Casa", "CasaRural", "CasaUrbana",
    "Apartamento", "Apartaestudio", "ApartamentoFamiliar",
    "Local", "LocalComercial", "Oficina"
]
#Se facilita el import y se usa el init para declarar la carpeta como un paquete o modulo para python