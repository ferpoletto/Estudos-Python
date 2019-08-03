from datetime import date
ano = int(input("Digite o ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano


if idade <= 9:
    categoria = 'Mirim'
elif idade > 9 and idade <= 14:
    categproa = 'Infantil'
elif idade > 14 and idade <= 19:
    categoria = 'Junior'
elif idade >19 and idade <= 25:
    categoria = 'Senior'
else:
    categoria = 'Master'

print(f'O atleta tem {idade} anos e sua categoria é {categoria}')