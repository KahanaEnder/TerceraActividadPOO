from Universidad import Persona
class Profesor(Persona):
    def __init__(self, nombre, direccion,departamento:str,categoria:str):
        super().__init__(nombre, direccion)
        self.departamento:str = departamento
        self.categoria:str = categoria
    def getDepartamento(self):
        print(f"{self.departamento}")
    def getCategoria(self):
        print(f"{self.categoria}")
    def setDepartamento(self,departamento:str):
        self.departamento = departamento
        return
    def setCategoria(self,categoria:str):
        self.categoria = categoria
        return