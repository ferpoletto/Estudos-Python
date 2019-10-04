#2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo, e mostre-o por extenso.
# Este número deverá variar entre 1 e 5. Se o usuário introduzir um número que não pertença a este intervalo,
# mostre a frase “número inválido”.

class numeros():
    def __init__(self):
        self.numero_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

    def num2sting(self, n):
        return self.numero_por_extenso[n]

    def executa(self):
        while True:
            numero = int(input('Digite um número entre 0-5:'))
            if numero >=0 and numero <= 5:
                break
            print('Tente novamente.')
