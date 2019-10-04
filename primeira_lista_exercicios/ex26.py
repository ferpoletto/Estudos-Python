#26 - Faça um programa que receba duas listas e retorne True se são iguais
# ou False caso contrário, além do número de # ocorrências do primeiro
# elemento da lista.


def numero_ocorrencias_primeiro_termo(lista):
    print(f"O primeiro elemento da lista ocorre {lista.count(lista[0])}x")


def comparar_listas(lista1, lista2):
    if lista1 == lista2:
        return True
    else:
        return False

lista1 = list(range(1, 20))
lista2 = list(range(1, 20))

numero_ocorrencias_primeiro_termo(lista1)
print(comparar_listas(lista1, lista2))
