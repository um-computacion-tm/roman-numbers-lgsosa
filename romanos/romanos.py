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



if __name__ == '__main__':
    unittest.main()