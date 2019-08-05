import random

lista = []

for i in range(4):
    lista.append(input("Digite um nome: "))

random.shuffle(lista)

print(f'A ordem de apresentação do trabalho será: {lista}')