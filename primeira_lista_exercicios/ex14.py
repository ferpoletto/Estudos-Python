#14 - Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).

tab = int(input("Digite o número para saber a tabuada: "))

print("--" * 10)
for i in range(10):
    print(f'{i+1} X {tab} = {(i + 1) * tab}')
print("--" * 10)