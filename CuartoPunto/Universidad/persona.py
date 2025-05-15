class Persona():
    def __init__(self,nombre:str,direccion:str):
        self.nombre:str = nombre
        self.direccion:str = direccion
    def getNombre(self):
        print(f"{self.nombre}")
    def getDireccion(self):
        print(f"{self.direccion}")
    def setNombre(self,nombre:str):
        self.nombre = nombre
        return
    def setDireccion(self,direccion:str):
        self.direccion = direccion
        return
