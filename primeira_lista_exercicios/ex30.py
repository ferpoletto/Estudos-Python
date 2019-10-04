#30 - Crie um dict com 5 nomes e idades, crie um segundo dict duplicando os itens.
primeiro = {}
aux = {}

for i in range(3):
    aux.clear()
    aux = {input('Digite o nome: '): int(input("Digite idade: "))}
    primeiro.update(aux.copy())
print(f"Primeiro dicionário: {primeiro}")
segundo = primeiro.copy()
print(f'Segundo dicionário: {segundo}')

