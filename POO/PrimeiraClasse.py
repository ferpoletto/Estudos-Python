class retangulo:

    def __init__(self):
        self.la = 0
        self.c = 0

    def area(self):
        return self.c * self.l


teste = retangulo()
teste.la = 2
teste.c = 2
print(teste.area())

teste2 = retangulo()
teste2.la = 4
teste2.c = 60
print(teste2.area())
