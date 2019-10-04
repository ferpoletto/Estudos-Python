#6 - Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar,
# e se é positivo ou negativo

class numeros():
    def verifica_par_impar(self, numero):
        if numero % 2 == 0:
            print('PAR')
        else:
            print('IMPAR')

    def verifica_positivo_negativo(self, numero):
        if numero >= 0:
            print('POSITIVO')
        else:
            print('NEGATIVO')

numero = float(input('Digite um numero: '))

minhaClasse = numeros()
minhaClasse.verifica_par_impar(numero)
minhaClasse.verifica_positivo_negativo(numero)
