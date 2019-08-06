num = cont = soma = 0
num = int(input('Digite um valor. [999 para sair]: '))
while num != 999:
    num = int(input('Digite um valor. [999 para sair]: '))
    if num != 999:
        soma += num
        cont +=1
print(f'Foram inseridos {cont} números, e a soma deles é {soma}')
