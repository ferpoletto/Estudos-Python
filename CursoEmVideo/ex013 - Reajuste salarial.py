salario = float(input('Digite o salário do funcionário R$ '))

print(f'O funcionário que ganhava R${salario:.2f}, com 15% de aumento passa a receber R${(salario + (salario * 15 / 100)):.2f}')
