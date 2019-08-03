oposto = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimenro do cateto adjacente: '))

print(f'A hipotenusa é {(((oposto ** 2) + (adj ** 2)) ** (1/2)):.2f}')