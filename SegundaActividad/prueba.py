from Inmuebles import *
class Prueba():
    if __name__ == "__main__":
        apto1 = ApartamentoFamiliar(103067,"Avenida-Santander-45-45",120,3,2,200000)
        apto1.calcularPrecioVenta(apto1._valorArea)
        aptestudio1 = Apartaestudio(12354,"Avenida Caracas 30-15",50)
        aptestudio1.calcularPrecioVenta(aptestudio1._valorArea)
        aptestudio1.imprimir()


