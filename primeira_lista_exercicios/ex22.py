# Crie a classe Imóvel, que possui um endereço e um preço.
# a. crie uma classe Novo, que herda Imóvel e possui um adicional no preço. Crie
# métodos de acesso e impressão deste valor adicional.
# b. crie uma classe Velho, que herda Imóvel e possui um desconto no preço. Crie
# métodos de acesso e impressão para este desconto.

class imovel():
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def imprimir(self):
        print(f'Preco = {self.preco}. Endereco = {self.endereco}')

class novo(imovel):

    def adicional(self, adicional):
        self.preco += adicional
        return self.preco

class velho(imovel):

    def desconto(self, desconto):
        self.preco -= desconto
        return self.preco