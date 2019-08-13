pessoas = list()
p = dict()

while True:
    p.clear()
    p['nome'] = input("Nome: ")

    while True:
        p['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if p['sexo'] in 'MF':
            break
        else:
            print('Erro. Digite M ou F')

    p['idade'] = int(input("Idade: "))
    pessoas.append(p.copy())

    while True:
        r = input('Deseja continuar? [S/N]: ').upper()[0]
        if r in 'SN':
            break
        else:
            print('Erro. Digite S ou N')

    if r == 'N':
        break
print(pessoas)

print(f'Ao todo temos {len(pessoas)} cadastradas.')
