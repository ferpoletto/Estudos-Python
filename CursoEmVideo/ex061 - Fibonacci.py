termos = int(input("Digite quantos números da sequência vc quer mostrar: "))
a = 0
b = 1
print(f'{a} > ', end='')
print(f'{b} > ', end='')
for i in range(termos - 2):
    c = b + a
    print(f'{c} > ', end='')
    a, b = b, c
print(f'Fim')
