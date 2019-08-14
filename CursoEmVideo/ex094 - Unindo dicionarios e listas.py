pessoas = list()
p = dict()
soma_idade = 0
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
    soma_idade += p['idade']
    while True:
        r = input('Deseja continuar? [S/N]: ').upper()[0]
        if r in 'SN':
            break
        else:
            print('Erro. Digite S ou N')

    if r == 'N':
        break


media_idade = soma_idade/len(pessoas)


print(pessoas)
print('-='*25)
print(f'Ao todo temos {len(pessoas)} cadastradas.')
print(f'A média de idade é {media_idade}')
print(f'A lista de pessoas que estão acima da média é: ')
for i in pessoas:
    if i['idade'] >= media_idade:
        print(i)
print(f'As mulheres cadastradas foram: ', end='')
for i in pessoas:
    if i['sexo'] == "F":
        print(i['nome'], end=' ')
