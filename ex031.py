distancia = float(input("Quantos km é o seu destino? "))

custo = 0.5 if distancia >= 200 else 0.45

print(f'O preço da viagem é de R${distancia*custo}')