from Universidad import Persona
class Estudiante(Persona):
    def __init__(self, nombre, direccion,carrera:str,semestre:int):
        super().__init__(nombre, direccion)
        self.carrera:str = carrera
        self.semestre:int = semestre
    def getCarrera(self):
        print(f"{self.carrera}")
    def getSemestre(self):
        print(f"{self.semestre}")
    def setCarrera(self,carrera:str):
        self.carrera = carrera
        return
    def setSemestre(self,semestre:int):
        self.semestre = semestre
        return