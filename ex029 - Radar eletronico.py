vel = float(input("Qual a velocidade atual do seu carro? "))

if vel <= 80:
    print("Bom dia, dirija com cuidado")
else:
    excesso = vel - 80
    multa = excesso * 7
    print(f'MULTADO! Você excedeu o limite permitido de 80Km/h. Você deve pagar uma multa de R${multa:.2f}')