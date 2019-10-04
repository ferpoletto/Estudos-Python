#3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
# O usuário deve informar dois números e o programa deve fazer as quatro operações.
#
# (modifique para calcular tudo no mesmo método, somando 1 ao resultado de cada operação)


class Calculadora():
    def todas_operacoes(self, n1, n2):
        print(f'{n1} + {n2} = {n1 + n2}')
        print(f'{n1} - {n2} = {n1 - n2}')
        print(f'{n1} * {n2} = {n1 * n2}')
        print(f'{n1} / {n2} = {n1 / n2}')

    def somar(selfn, n1, n2):
        return n1+n2

    def diminuir(self, n1, n2):
        return n1-n2

    def multiplicar(self, n1, n2):
        return n1*n2

    def dividir(self, n1, n2):
        return n1/n2

    def executa(self):
        operacao = ''

        while operacao != 'S':
            operacao = input('+ > Somar\n'
                             '- > Diminuir\n'
                             '* > Multiplicar\n'
                             '/ > Dividir\n'
                             '** > TODAS OPERAÇÕES\n'
                             'S > Sair\n'
                             'Digite a operação desejada:\n')

            minha_calculadora = Calculadora()

            if operacao == 'S':
                exit()
            else:
                n1 = int(input("Digite N1: "))
                n2 = int(input("Digite N2: "))

            if operacao == '+':
                (minha_calculadora.somar(n1, n2))
            elif operacao == '-':
                (minha_calculadora.diminuir(n1, n2))
            elif operacao == '*':
                (minha_calculadora.multiplicar(n1, n2))
            elif operacao == '/':
                (minha_calculadora.dividir(n1, n2))
            elif operacao == '**':
                (minha_calculadora.todas_operacoes(n1, n2))
