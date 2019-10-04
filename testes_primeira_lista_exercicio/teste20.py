"""20 - Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter  um método  aumenta_salario.
Crie duas subclasses da classe funcionário, programador  e  analista, implementando o método  nas duas subclasses.
Para o programador some ao atributo salário mais 20 e ao analista some ao salário mais 30,  mostrando na tela o valor.
Depois disso, crie uma classe de testes instanciando os objetos programador e analista e chame o método  aumenta_salario
de cada um."""
import unittest


class Funcionarios():
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.salario = 1000

    def aumentaSalario(self):
        return self.salario + 0


class Programador(Funcionarios):

    def aumentaSalario(self):
        self.salario += 20
        return self.salario


class Analista(Funcionarios):

    def aumentaSalario(self):
        self.salario += 30
        return self.salario


class main():

    def __init__(self):
        demetrius = Analista()
        print(demetrius.salario)
        print(demetrius.aumentaSalario())
        print(demetrius.salario)

        rodolfo = Programador()
        print(rodolfo.salario)
        print(rodolfo.aumentaSalario())
        print(rodolfo.salario)


# if __name__ == '__main__':
#     main()

class TesteFuncionario(unittest.TestCase):

    def test_programador(self):
        prog = Programador()
        resultado = prog.aumentaSalario()
        self.assertEqual(resultado, 1020)

    def test_analista(self):
        sandro = Analista()
        resultado = sandro.aumentaSalario()
        self.assertEqual(resultado, 1030)

