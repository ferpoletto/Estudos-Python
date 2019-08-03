from datetime import date
ano_nascimento = int(input('Digite ano do nascimento: '))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {date.today().year}')
print(f'Você se alistou em {ano_nascimento+18}')