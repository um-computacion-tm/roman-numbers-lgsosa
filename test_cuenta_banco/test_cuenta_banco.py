import unittest

from test_cuenta_banco import (
    CajaAhorro,
    CuentaCorriente,
    SaldoInsuficiente,
    ExcedeDescubiertoException,
)


class TestCuentaCorriente(unittest.TestCase):
    def setUp(self):
        self.cuenta_corriente = CuentaCorriente()

    def test_inicio_cuenta_corriente(self):
        self.assertEqual(
            self.cuenta_corriente.saldo,
            0,
        )

    def test_deposito_cuenta_corriente(self):
        self.cuenta_corriente.deposito(100)
        self.assertEqual(
            self.cuenta_corriente.saldo,
            100,
        )

    def test_retiro_cuenta_corriente(self):
        self.cuenta_corriente.deposito(100)
        self.cuenta_corriente.retiro(80)
        self.assertEqual(
            self.cuenta_corriente.saldo,
            20,
        )

    def test_retiro_cuenta_corriente_en_descubierto(self):
        self.cuenta_corriente.deposito(100)
        self.cuenta_corriente.retiro(200)
        self.assertEqual(
            self.cuenta_corriente.saldo,
            -100,
        )

    def test_retiro_cuenta_corriente_fuera_descubierto(self):
        self.cuenta_corriente.deposito(100)
        with self.assertRaises(ExcedeDescubiertoException):
            self.cuenta_corriente.retiro(500)
        self.assertEqual(
            self.cuenta_corriente.saldo,
            100,
        )


class TestCajaAhorro(unittest.TestCase):

    def setUp(self):
        self.caja_ahorro = CajaAhorro()

    def test_inicio_caja_ahorro(self):
        self.assertEqual(
            self.caja_ahorro.saldo,
            0,
        )

    def test_deposito_caja_ahorro(self):
        self.caja_ahorro.deposito(100)
        self.assertEqual(
            self.caja_ahorro.saldo,
            100,
        )

    def test_segundo_deposito_caja_ahorro(self):
        self.caja_ahorro.deposito(100)
        self.caja_ahorro.deposito(1000)
        self.assertEqual(
            self.caja_ahorro.saldo,
            1100,
        )

    def test_deposito_dos_cajas_ahorro(self):
        caja_ahorro_2 = CajaAhorro()
        self.caja_ahorro.deposito(100)
        caja_ahorro_2.deposito(200)
        self.assertEqual(
            self.caja_ahorro.saldo,
            100,
        )

        self.assertEqual(
            caja_ahorro_2.saldo,
            200,
        )

    def test_retiro_cajas_ahorro(self):
        self.caja_ahorro.deposito(100)
        self.caja_ahorro.retiro(80)
        self.assertEqual(
            self.caja_ahorro.saldo,
            20,
        )

    def test_retiro_cajas_ahorro_sin_saldo(self):
        with self.assertRaises(SaldoInsuficiente):
            self.caja_ahorro.retiro(80)
        self.assertEqual(
            self.caja_ahorro.saldo,
            0,
        )


if __name__ == '__main__':
    unittest.main()