#18 - Crie uma classe animal com o método comer, este método deve  escrever na tela "o animal esta comendo".
# Depois disso crie as classes cachorro, cavalo e gato e implemente o método comer de acordo com o que cada animal come.
# Crie uma classe AnimalTeste e coloque os três animais dentro de uma lista de animais e chame o método comer
# polimorficamente (com um for)

class animal:

    def comer(self):
        print('O animal está comendo')

class cavalo(animal):

    def comer(self):
        print('O cavalo está comendo grama')

class cachorro(animal):

    def comer(self):
        print('O cachorro está comendo ração')

class gato(animal):

    def comer(self):
        print('O gato está comendo rato')


cavalo = cavalo()
cachorro = cachorro()
gato = gato()

lista = [cavalo, cachorro, gato]


for i in lista:
    i.comer()

