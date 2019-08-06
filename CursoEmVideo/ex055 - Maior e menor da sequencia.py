pesos = []
for i in range(5):
    pesos.append(float(input(f'Digite o peso da pessoa {i+1}: ')))

print(f'O maior peso lido foi de {max(pesos)}Kg')
print(f'O menor peso lido foi de {min(pesos)}Kg')