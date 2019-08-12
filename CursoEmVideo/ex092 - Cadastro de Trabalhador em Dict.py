trabalhador = dict()

trabalhador['nome'] = input("Digite o nome: ")
trabalhador['ano_nasc'] = int(input("Digite o ano de nascimento: "))
trabalhador['carteira_trab'] = int(input("Digite o numero da carteira de trabalho(0 não tem): "))

if trabalhador['carteira_trab'] != 0:
    trabalhador['ano_contr'] = int(input("Digite o ano da contratação: "))
    trabalhador['salario'] = float(input("Digite o salario:"))
    trabalhador['aposentadoria'] = 35+trabalhador['ano_contr']

print('-='*25)
for k, v in trabalhador.items():
    print(f'{k} = {v}')
