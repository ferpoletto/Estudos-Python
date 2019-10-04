#15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles.
lista = []
for i in range(10):
    lista.append(int(input(f"Digite o {i + 1}o número:")))

print(f'O maior número é {max(lista)}')
