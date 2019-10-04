#24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas,
# isto é, 1º da 1ª lista, 1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista.

lista1 = []
lista2 = []
uniao = []

for i in range(5):
    lista1.append((int(input(f"Digite o {i+1}o valor da lista 1: "))))
    lista2.append((int(input(f'Digite o {i+1}o valor da lista 2: '))))

print("Lista 1: ", lista1)
print("Lista 2: ", lista2)

for i in range(len(lista1)):
    uniao.append(lista1[i])
    uniao.append(lista2[i])

print("Lista Uniao: ", uniao)
