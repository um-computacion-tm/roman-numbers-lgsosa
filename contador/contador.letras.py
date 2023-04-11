import unittest

letr = 'Hola como estas'

def cont_letras (letr):
    letras=0
    for z in letr:
        if z.isalpha():
            letras +=1
    return letras

print (cont_letras(letr))

class contador_letras (unittest.TestCase):
    def test_letras(self):
        resultado=cont_letras
        self.assertAlmostEqual(resultado,(cont_letras))

if __name__ == '__main__':
    unittest.main()