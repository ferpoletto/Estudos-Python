import random

chute = int(input("Tente descobrir que número eu pensei (0 até 10): "))

num_pensado = random.randint(0,11)
cont = 0
while chute != num_pensado:
    if chute < num_pensado:
        print('Mais...Tente novamente')
        chute = int(input("Entre 0-10: "))
        cont += 1
    else:
        print('Menos...Tente novamente')
        chute = int(input("Entre 0-10: "))
        cont += 1

print(f'Parabéns, vc acertou o número {num_pensado} na {cont}')