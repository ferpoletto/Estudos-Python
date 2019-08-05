tabuada = int(input('Digite um número para ver sua tabuada: '))

print('----------')
for i in range(10):
    print(f'{tabuada} X {i+1} = {tabuada * (i+1)}')
print('----------')