dias = int(input('Quantos dias o carro foi alugado? '))

km = float(input('Quantos km rodados? '))

total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é R${total:.2f}')