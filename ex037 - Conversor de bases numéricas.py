num = int(input('Digite um número : '))

print('[1] BINARIO\n'
      '[2] OCTAL\n'
      '[3] HEXADECIMAL\n')
opcao = int(input('Digite sua opção:'))

if opcao == 1:
    print(f'{num} em binário é {bin(num)}')

elif opcao == 2:
    print(f'{num} em octal é {oct(num)}')

elif opcao == 3:
    print(f'{num} em hexadecimal é {hex(num)}')

else:
    print('Opcao inválida.')
