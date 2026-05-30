class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print(f"Se depositaron {cantidad}. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            return cantidad
        else:
            print("Fondos insuficientes")

    def consultarSaldo(self):
        return self.saldo

    def mostrarInformacion(self):
        return f"Titular: {self.titular}, Saldo: ${self.saldo}"


cuenta1 = CuentaBancaria("Ricardo Garcia", "21100001", 1000.0)
print(cuenta1.mostrarInformacion())
cuenta1.depositar(500.0)
cuenta1.retirar(2000.0)
cuenta1.depositar(300.0)
print(cuenta1.mostrarInformacion())
