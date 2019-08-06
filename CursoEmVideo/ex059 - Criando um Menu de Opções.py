num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

op = ''

while op not in [1, 2, 3, 4, 5]:
    op = int(input('[1] Somar\n'
          '[2] multiplicar\n'
          '[3] maior \n'
          '[4] novos numeros \n'
          '[5] SAIR \n'
          'Qual sua opcao? '))

    if op == 5:
        break

    elif op == 4:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))

    elif op == 3:
        print(f'O maior é {max([num1, num2])}')

    elif op == 2:
        print(f'Multiplicação {num1*num2}')

    else:
        print(f'Soma {num1+num2}')

    op = ''

print(op)