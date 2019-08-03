lista = []
for i in range(6):
    lista.append(int(input("Digite um valor: ")))

print(lista)
soma = 0
for numeros in lista:
    if numeros %2 == 0:
        soma += numeros

print(f'Soma {soma}')