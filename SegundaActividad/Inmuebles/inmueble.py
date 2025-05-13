class Inmueble:
    def __init__(self, direccion, metros_cuadrados, precio):
        self.direccion = direccion
        self.metros_cuadrados = metros_cuadrados
        self.precio = precio

    def imprimir(self):
        print(f"Dirección: {self.direccion}")
        print(f"Metros cuadrados: {self.metros_cuadrados}")
        print(f"Precio: {self.precio}")
