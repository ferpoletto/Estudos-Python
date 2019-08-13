jogador = {}

jogador['nome'] = input("Digite o nome do jogador: ")

partidas = int(input(f"Digite quantas partidas {jogador['nome']} jogou: "))
lista=[]
for i in range(partidas):
    lista.append(int(input(f"Quantos gols na partida {i+1}: ")))

jogador['gols'] = lista[:]
jogador['total'] = sum(lista)
print(f'-='*30)
print(jogador)
print(f'-='*30)
for k, v in jogador.items():
    print(f'{k} = {v}')
print(f'-='*30)

print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for i in range(len(lista)):
    print(f'Na partida {i+1}, fez {lista[i]}')
print(f'Foi um total de {jogador["total"]} gols.')