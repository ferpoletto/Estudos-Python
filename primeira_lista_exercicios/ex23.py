#23 - Crie uma programa que recebe uma lista qualquer e:
#a. retorne o maior elemento
#b. retorne a soma dos elementos
#c. retorne o número de ocorrências do primeiro elemento da lista
#d. retorne a média dos elementos


def maior_valor(self):
    return max(lista)

def soma(self):
    return sum(lista)

lista = []

for i in range(5):
    lista.append(int(input("Digite um numero: ")))

print("Máximo valor = ", maior_valor(lista))

print("A soma dos elementos da lista é", soma(lista))

print(f"O primeiro elementa da lista ({lista[0]}) ocorre {lista.count(lista[0])}x")
print(f"A média dos elementos é {soma(lista) / len(lista)}")
