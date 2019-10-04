import unittest
from primeira_lista_exercicios.ex02 import numeros

class num2stringtest(unittest.TestCase):

    def test_num2string(self):
        teste = numeros()
        resultado = teste.num2sting(2)
        self.assertEqual(resultado, 'dois')
