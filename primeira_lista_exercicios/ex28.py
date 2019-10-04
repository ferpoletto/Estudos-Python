#28 - Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos valores da lista.
# Exemplo: lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0). Valor mais próximo da média = 7.5

def media(lista):
    return float(sum(lista)) / max(len(lista), 1)

lista = [2.5, 3, 10.0, 4.0]


diff = []
for i in range(len(lista)):
    diff.append(abs(lista[i] - media(lista)))

print(f'A média é {media(lista):.2f}. E o valor mais proximo da média é {lista[diff.index(min(diff))]}')
