#13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres
# (considere que as idades dos homens serão sempre diferentes entre si, bem
# como as das mulheres). Calcule e escreva a soma das idades do homem mais
# velho com a mulher mais nova, e o produto das idades do homem mais novo
# com a mulher mais velha.

homens = [int(input("Digite a idade do primeiro homem: ")),
          int(input("Digite a idade do segundo homem: "))]

mulheres = [int(input("Digite a idade da primeira mulher: ")),
            int(input("Digite a idade da segunda mulher: "))]

print(f'Idade do homem mais novo = {min(homens)}\n'
      f'Idade do homem mais velho = {max(homens)}\n'
      f'Idade da mulher mais nova = {min(mulheres)}\n'
      f'Idade da mulher mais velha = {max(mulheres)}')

print(f'A soma da mulher mais nova com homem mais velho é {(min(mulheres) + (max(homens)))}')
print(f'O produto da idade do homem mais novo com a mulher mais velha é {(min(homens) * (max(mulheres)))}')