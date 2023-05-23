import unittest
from unittest.mock import patch
from main_cuenta_banco import main

class TestMain(unittest.TestCase):
    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['A', 'C', 'Q'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    def test_saldo_caja_ahorro_consulta(self, mock_print, mock_input):
        main()
        mock_print.assert_called_once_with(
            'El saldo de la cuenta es: 0'
        )

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['C', 'C', 'Q'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    def test_saldo_cuenta_corriente_consulta(self, mock_print, mock_input):
        main()
        mock_print.assert_called_once_with(
            'El saldo de la cuenta es: 0'
        )



if __name__ == '__main__':
    unittest.main()

