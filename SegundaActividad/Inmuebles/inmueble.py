class Inmueble:
    #constructor
    def __init__(self,id_inmobiliario:int,direccion:str,area:int):
        self._id_inmobiliario = id_inmobiliario
        self._direccion = direccion
        self._area = area
        self._precioVenta:float

    def calcularPrecioVenta(self, valorArea:float):
        self._precioVenta = self._area * valorArea
        print(self._precioVenta)

    def imprimir(self):
        print(f"Dirección: {self._direccion}")
        print(f"Metros cuadrados: {self._area}")
        print(f"Identificación Inmobiliaria: {self._id_inmobiliario}")
        print(f"Precio de venta: {self._precioVenta}")