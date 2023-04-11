#con listas, tuplas y diccionarios.
import unittest

lista=['ojo','cabeza','craneo']

def contador (lista):
    cont= len((lista))
    return cont


class contador_de_palabras(unittest.TestCase):
    def test_contador(self):
        resultado = contador
        self.assertEqual (resultado,(contador))

if __name__ == '__main__':
    unittest.main()