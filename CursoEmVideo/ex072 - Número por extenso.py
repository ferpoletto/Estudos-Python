while True:
    num = int(input("Digite um número entre 0-20: "))
    while num > 20 or num < 0:
        num = int(input("Tente novamente. Digite um número entre 0-20: "))

    extenso = ['Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
               'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
               'Dezoito', 'Dezenove', 'Vinte']

    print(f'Voce digitou o número {extenso[num]}')
    op = input("Deseja continuar? S/N").upper()
    if op == 'N':
        break
