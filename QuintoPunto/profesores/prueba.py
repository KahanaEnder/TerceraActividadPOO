from profesores import ProfesorTitular
class Prueba():
    if __name__ == "__main__":
        profesor1 = ProfesorTitular()
        profesor1._imprimir()
        profesor2 = profesor1  # No hay casting, en java si
        profesor2._imprimir()