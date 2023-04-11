import unittest

def roman_to_decimal(roman):
    total = 0
    for letter in roman:
        if letter in roman:
            if letter =='I':
                total +=1
            elif letter == 'V':
                if total >0:
                    total =-1
                total += 5
            elif letter == 'X':
                if total >0:
                    total =-1
                total += 10
            elif letter == 'IV':
                total == 4
    return total
            
        

        

class TestRomanDecimal(unittest.TestCase):
    def test_I (self):
        resultado =  roman_to_decimal('I')
        self.assertEqual(resultado,1)
        resultado =  roman_to_decimal('II')
        self.assertEqual(resultado,2)
        resultado =  roman_to_decimal('III')
        self.assertEqual(resultado,3)
    def test_IV(self):
        resultado =  roman_to_decimal('IV')
        self.assertEqual(resultado,5)
    def test_V(self):
        resultado =  roman_to_decimal('V')
        self.assertEqual(resultado,5)
    def test_X (self):
        resultado =  roman_to_decimal('X')
        self.assertEqual(resultado,10)
        

if __name__ == '__main__':
    unittest.main()