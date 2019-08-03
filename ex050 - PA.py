primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print('=' * 15)
print('10 TERMOS DE UMA PA')
print('=' * 15)
print(primeiro_termo, end='')

for i in range(9):

    print('>', end='')
    print(primeiro_termo + razao, end='')
    primeiro_termo = primeiro_termo + razao
