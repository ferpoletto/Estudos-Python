from datetime import date

ano_atual = date.today().year

anos = []

for i in range(7):
    anos.append(int(input(f'Digite o ano que a {i+1} nasceu: ')))

idades = []

for ano in anos:
    idades.append((ano_atual-ano))

velhos = 0
jovens = 0

for idade in idades:
    if idade >= 21:
        velhos += 1
    else:
        jovens += 1

print(f'Jovens = {jovens} pessoas')
print(f'Velhos = {velhos} pessoas')