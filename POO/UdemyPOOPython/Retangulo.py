class Retangulo():

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def get_area(self):
        return self.altura * self.largura

r = Retangulo(10, 20)

print(r.get_area())
