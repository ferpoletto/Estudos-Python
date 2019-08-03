import random
chute = int(input("Tente descobrir que número eu pensei: "))

num_pensado = random.randint(1,5)

if num_pensado == chute:
    print('Você acertou!')
else:
    print("Você errou!")