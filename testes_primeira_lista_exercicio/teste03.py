import unittest
from primeira_lista_exercicios.ex03 import Calculadora

class testCalculadora(unittest.TestCase):

    def test_soma(self):
        calc = Calculadora()
        resultado = calc.somar(2,3)
        self.assertEqual(resultado, 5)

    def test_diminui(self):
        calc = Calculadora()
        resultado = calc.diminuir(2,3)
        self.assertEqual(resultado, -1)

    def test_multiplicar(self):
        calc = Calculadora()
        resultado = calc.multiplicar(2,3)
        self.assertEqual(resultado, 6)

    def test_dividir(self):
        calc = Calculadora()
        resultado = calc.dividir(40,10)
        self.assertEqual(resultado, 4)

