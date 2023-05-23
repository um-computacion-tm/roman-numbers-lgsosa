class SaldoInsuficiente(Exception):
    pass

class ExcedeDescubiertoException(Exception):
    pass


class CuentaBanco:

    def deposito(self, monto):
        self.saldo += monto


class CuentaCorriente(CuentaBanco):

    def __init__(self):
        self.saldo = 0
        self.descubierto = -200

    def retiro(self, monto):
        if self.saldo - monto < self.descubierto:
            raise ExcedeDescubiertoException('Excede saldo en descubierto')
        self.saldo -= monto

class CajaAhorro(CuentaBanco):

    def __init__(self):
        self.saldo = 0

    def retiro(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficiente('Saldo insuficiente')
        self.saldo -= monto