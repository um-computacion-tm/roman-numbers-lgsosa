import unittest
class NumeroMenorA1Exception(Exception):
    pass    

class NumeroMayorA10Exception(Exception):
    pass

def calcular_1_al_10(numero):
    if(numero < 1):
        raise NumeroMenorA1Exception ('numero es menor que 1')
    if (numero > 10):
        raise NumeroMayorA10Exception ('numero es mayor que 10')
    return 'tu numero' + str(numero) + 'es de 1 al 10'
    
while True:
    try:
        numero = int(input('ingrese un numero del 1 al 10: '))
        calcular_1_al_10(numero)
        break
    except ValueError as value_error_excepcion:
        print('burro: por favor ingrese un numero')
    except NumeroMenorA1Exception as mi_excepcion:
        print('burro: ' + str(mi_excepcion))  
    except NumeroMayorA10Exception as mi_excepcion:
        print('burro: ' + str(mi_excepcion))
            
            
class TestNuemeroDel1Al10(unittest.TestCase):
    def test_feliz(self):
        result = calcular_1_al_10(5)
        self.assertAlmostEqual(
            result, 
        '   tu numero' + str(numero) + 'es de 1 al 10'
        )  
          
            
    def test_da_error_numero_es_menor_1(self):
       with self.assertRaises(Exception):
           result = calcular_1_al_10(-14)
           
    def test_da_error_numero_es_mayor_10(self):
        with self.assertRaises(Exception):
              result = calcular_1_al_10(14)       

if __name__ == '__main__':
    unittest.main()