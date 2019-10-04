#17 - Cria uma lista para armazenar 5 nomes fixos. Após inserir os 5 nome da lista mostre-os
# no console (utilize um for).

lista = []

for i in range(5):
    lista.append(input("Digite o nome: "))

print(lista)