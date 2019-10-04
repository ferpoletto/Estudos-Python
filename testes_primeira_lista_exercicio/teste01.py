import unittest
from primeira_lista_exercicios.ex01 import validacao

class idadeTest(unittest.TestCase):

    def test_valida_18anos(self):
        idade = validacao()
        resultado = idade.valida_idade_maior_18(18)
        self.assertEqual(resultado, 'Maior de idade')

    def test_valida_17anos(self):
        idade = validacao()
        resultado = idade.valida_idade_maior_18(17)
        self.assertEqual(resultado, 'Menor de idade')

    def test_valida_27anos(self):
        idade = validacao()
        resultado = idade.valida_idade_maior_18(27)
        self.assertEqual(resultado, 'Maior de idade')
