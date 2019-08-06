frase = input("Digite uma frase: ").strip().upper()
print(f'Você digitou a frase {frase}')

palavras = frase.split()
print(palavras)
semespaco = ''.join(palavras)
print(semespaco)
inverso = ''

for i in range(len(semespaco)-1, -1, -1):
    inverso += semespaco[i]


if frase == inverso:
    print(f'A frase digitada é um palíndromo')
else:
    print(f'A frase digita não é um palíndromo')

print(f'O inverso de "{frase}" é "{inverso}"')