r1 = int(input("Digite o R1: "))
r2 = int(input("Digite o R2: "))
r3 = int(input("Digite o R3: "))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r2 + r1:
    print("è triangulo")
else:
    print('Não é triangulo')

