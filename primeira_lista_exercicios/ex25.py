#25 - Faça uma função que receba uma lista e exiba os elementos da última metade na
# frente dos elementos da primeira metade

def inverte_lista(lista):
    lista_invertida = lista[int((len(lista)/2)):]
    lista_invertida.extend(lista[:int((len(lista)/2))])
    return lista_invertida

lista = []
while True:
    lista.append(input("Digite um numero para adicionar a lista: "))
    op = input("Deseja adicionar mais numeros? [S/N]: ").upper().strip()

    if op == "N":
        break

print(inverte_lista(lista))
