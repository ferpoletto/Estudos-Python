import random

lista = ('PEDRA', 'PAPEL', 'TESOURA')

computador = random.randint(0,2)

jogador = int(input('0 - PEDRA\n'
                    '1 - PAPEL\n'
                    '2 - TESOURA\n'
                    'Digite sua jogada: '))
print('=-'*12)
print(f'Computador jogou {lista[computador]}')
print(f'Jogador jogou {lista[jogador]}')
print('=-'*12)

if computador == 0:
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Jogador ganhou.')
    elif jogador == 2:
        print('Computador ganhou')
    else:
        print('Jogada inválida')

elif computador == 1:
    if jogador == 0:
        print('Computador ganhou')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Computador ganhou')
    else:
        print('Jogada inválida')

elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Empatou!')
    else:
        print('Jogada inválida')
