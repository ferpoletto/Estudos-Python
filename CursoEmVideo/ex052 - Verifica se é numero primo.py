num = int(input("Digite um número: "))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        cont += 1

if cont <= 2:
    print(f'Número {num } é primo!')
else:
    print(f'Número {num} não é primo!')
