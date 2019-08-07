while True:
    tabuada = int(input("Digite um número para saber sua tabuada: "))

    if tabuada < 0:
        break

    for i in range(1,11):
        print(f'{tabuada} X {i} = {tabuada * (i)}')

