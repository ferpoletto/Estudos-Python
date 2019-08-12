from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}


print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} = {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking')
print(ranking)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')