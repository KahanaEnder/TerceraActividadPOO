class Cuenta(): 

    #atributos

    _saldo:float
    _numeroConsignaciones:int = 0
    _numeroRetiros:int = 0
    _tasaAnual:float
    _comisionMensual:float = 0

    #constructor

    def __init__(self,saldo:float,tasaAnual:float):

        self._saldo = saldo
        self._tasaAnual = tasaAnual

    #metodos

    def consignar(self,valor:float):
        if valor > 0:
            self._saldo += valor
            self._numeroConsignaciones += 1
        else:
            return

    def retirar(self,valor:float):
        if self._saldo > 0 and valor < self._saldo and valor > 0:
            self._saldo -= valor
            self._numeroRetiros += 1
        else:
            return


    def calcularInteresMensual(self):
        tasaMensual:float = self._tasaAnual / 12
        interesMensual:float = tasaMensual * self._saldo
        self._saldo += interesMensual

    def extractoMensual(self):
        self._saldo -= self._comisionMensual
        self.calcularInteresMensual()

#clase hija ahorros

class CuentaAhorros(Cuenta):

    pass

#clase hija corriente

class CuentaCorriente(Cuenta):

    pass




if __name__ == "__main__":
    cuenta1 = Cuenta(0,10)
    cuenta1.consignar(123)
    cuenta1.retirar(40)
    cuenta1.calcularInteresMensual()
    cuenta1.extractoMensual()
    print(f"Saldo: {cuenta1._saldo}\n Número de consignaciones: {cuenta1._numeroConsignaciones}\n Número de retiros: {cuenta1._numeroRetiros}\n Tasa Anual: {cuenta1._tasaAnual}\n Comision Mensual: {cuenta1._comisionMensual} ")