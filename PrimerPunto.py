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
    #atributos
    _activa:bool
    #metodos
    def __init__(self, saldo, tasaAnual):
        super().__init__(saldo, tasaAnual)
        self._activa = self._saldo >= 10000
    def consignar(self, valor):
        if self._activa:
            super().consignar(valor)
            self._activa = self._saldo >= 10000

    def retirar(self, valor):
        if self._activa:
            super().retirar(valor)
            self._activa = self._saldo >= 10000

    def extractoMensual(self):
        if self._numeroRetiros > 4:
            self._comisionMensual += (self._numeroRetiros - 4) * 1000
        super().extractoMensual()
        self._activa = self._saldo >= 10000

    def imprimir(self):
        total_transacciones = self._numeroConsignaciones + self._numeroRetiros
        print(f"Cuenta de Ahorros:\nSaldo: ${self._saldo:.2f}\nComisión mensual: ${self._comisionMensual:.2f}\nTransacciones: {total_transacciones}\nActiva: {self._activa}")


#clase hija corriente

class CuentaCorriente(Cuenta):
    _sobregiro:int

    def __init__(self, saldo, tasaAnual):
        super().__init__(saldo, tasaAnual)
        self._sobregiro = 0
        
    def retirar(self, valor: float):
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
            else:
                self._sobregiro += (valor - self._saldo)
                self._saldo = 0
            self._numeroRetiros += 1

    def consignar(self, valor: float):
        if valor > 0:
            if self._sobregiro > 0:
                if valor >= self._sobregiro:
                    valor -= self._sobregiro
                    self._sobregiro = 0
                else:
                    self._sobregiro -= valor
                    valor = 0
            self._saldo += valor
            self._numeroConsignaciones += 1

    def imprimir(self):
        total_transacciones = self._numeroConsignaciones + self._numeroRetiros
        print(f"Cuenta Corriente:\nSaldo: ${self._saldo:.2f}\nSobregiro: ${self._sobregiro:.2f}\nComisión mensual: ${self._comisionMensual:.2f}\nTransacciones: {total_transacciones}")




#metodo main
if __name__ == "__main__":
    cuenta1 = Cuenta(0,10)
    cuenta1.consignar(123)
    cuenta1.retirar(40)
    cuenta1.calcularInteresMensual()
    cuenta1.extractoMensual()
    print(f"Saldo: {cuenta1._saldo}\n Número de consignaciones: {cuenta1._numeroConsignaciones}\n Número de retiros: {cuenta1._numeroRetiros}\n Tasa Anual: {cuenta1._tasaAnual}\n Comision Mensual: {cuenta1._comisionMensual} ")
    cuenta2 = CuentaAhorros(12000,10)
    cuenta2.consignar(1000)
    cuenta2.retirar(1000)
    cuenta2.extractoMensual()
    cuenta2.imprimir()