#5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo),
# se é par ou ímpar

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
