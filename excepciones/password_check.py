import unittest

class PasswordTooShortException(Exception):
    pass


def validar_password(password):
    # ACA HAY QUE VALIDAR!!!
    # al menos 8 caracteres
    if len(password) < 8:
        raise PasswordTooShortException()
    # alguna letras
    # al menos una Mayuscula
    # al menos una minuscula
    # al menos un simbolo
    # al menos un numero
    for caracter in password:
        pass

    # HASTA ACA VALIDAMOS...
    return True



class TestPassword(unittest.TestCase):
    def test_valida(self):
        valida = validar_password('Hola1123$')
        self.assertTrue(valida)

    def test_muy_corta(self):
        with self.assertRaises(PasswordTooShortException):
            validar_password('H123$')


if __name__ == '__main__':
    unittest.main()