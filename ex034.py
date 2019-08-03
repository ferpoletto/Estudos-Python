salario = float(input('Digite o salário: '))

aumento = 10 if salario >= 1250 else 15

print(f'Salario atual R${salario:.2f}\n'
      f'Salário com aumento R${salario*aumento/100 + salario:.2f}')