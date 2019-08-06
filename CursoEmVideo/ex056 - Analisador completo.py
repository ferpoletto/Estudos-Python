cadastro = []

for i in range(4):
    aux = []
    print('='*5, i+1, 'a Pessoa', '='*5)
    aux.append(input('Nome: '))
    aux.append(int(input('Idade: ')))
    aux.append(input('Sexo [F/M]: '))
    cadastro.append(aux[:])

soma_das_idades = 0
maior_idade_M = 0
contador_menor20_F = 0

for i in range(4):
    soma_das_idades += cadastro[i][1]
    if cadastro[i][2] == 'M':
        if cadastro[i][1] > maior_idade_M:
            maior_idade_M = cadastro[i][1]
            index = i
    elif cadastro[i][2] == "F" and cadastro[i][1] < 20:
        contador_menor20_F += 1


media_das_idades = soma_das_idades/4

print(f'\n\nA média de idade do grupo é de {media_das_idades} anos')
print(f'O homem mais velho tem {cadastro[index][1]} anos e se chama {cadastro[index][0]}')
print(f'Ao todo são {contador_menor20_F} mulheres com menos de 20 anos.')

