valor_da_casa = float(input('Digite o valor da casa R$'))
salario = float(input('Digite o salário: '))
anos_para_pagar = int(input('Quando anos deseja pagar? '))

parcelas = anos_para_pagar * 12

prestacao = valor_da_casa / parcelas

print(f'Para pagar uma casa de R${valor_da_casa} em {anos_para_pagar} anos a prestação será de R${prestacao:.2f}')

if prestacao > salario * 0.3:
    print('EMPRESTIMO NEGADO')

else:
    print('EMPRESTIMO ACEITO')