import random
lista = []
for i in range(5):
    lista.append(input("Digite um nome: "))

print(f'O nome sorteado foi: {random.choice(lista)}')