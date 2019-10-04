#16 - Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA e
# apresente o valor do volume de uma caixa retangular. Utilize para o cálculo a
# fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.

def calcula_volume_caixa(c, l, a):
    return c * l * a

c = float(input("Digite o comprimento: "))
l = float(input("Digite a largura: "))
a = float(input("Digite a altura: "))

print(f'O volume dessa caixa é {calcula_volume_caixa(c, l, a)}m3')