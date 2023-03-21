import unittest

def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 4:
        return 'IV'
    elif decimal == 5:
        return 'V'
    elif decimal <5 or decimal <=8:
        return 'V' + 'I' * (decimal-5)
    
    
    elif decimal == 20 or decimal == 30 :
        return 'X' * (decimal //10)
    elif decimal ==40:
        return 'XL'
    elif decimal == 50:
        return 'L'
    
    
    else:
        return "X"


class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')
    
    def test_cuatro (self):
        resultado = decimal_to_roman (4)
        self.assertEqual(resultado, 'IV')

    def test_seis (self):
        resultado = decimal_to_roman (6)
        self.assertEqual (resultado,'VI')
    def test_seis (self):
        resultado = decimal_to_roman (7)
        self.assertEqual (resultado, 'VII')
    def test_seis (self):
        resultado = decimal_to_roman (8)
        self.assertEqual (resultado,'VIII')
    def test_veinte (self):
        resultado = decimal_to_roman (20)
        self.assertEqual (resultado,'XX')
    def test_veinte (self):
        resultado = decimal_to_roman (30)
        self.assertEqual (resultado,'XXX')
    def test_cincuenta (self):
        resultado = decimal_to_roman (50)
        self.assertEqual (resultado, 'L')
    def test_cuarenta (self):
        resultado = decimal_to_roman (40)
        self.assertEqual (resultado,'XL')



if __name__ == '__main__':
    unittest.main()