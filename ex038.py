n1 = int(input('Digite número:'))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n2} é maior que {n1}')
else:
    print(f'Numeros iguais')