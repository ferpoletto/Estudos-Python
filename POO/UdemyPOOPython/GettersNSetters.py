class Retangulo():

    def __init__(self, largura, altura):
        # self.largura = 0
        # self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_largura(self, num):
        if not((num > 0) and (isinstance(num, int))):
            raise ValueError(f"Largura Inválida {num}")
        self.largura = num

    def set_altura(self, num):
        if not(num > 0) and (isinstance(num, int)):
            raise ValueError(f"Altura Inválida {num}")
        self.altura = num

    def get_area(self):
        return self.largura * self.altura

a = Retangulo(30,10)

print(a.get_area())
