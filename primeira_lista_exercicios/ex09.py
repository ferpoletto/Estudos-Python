#9 - faça um método que receba um número X e uma palavra no console e repita x vezes a essa
# frase.

def repetidor(x, palavra):
    for i in range(x):
        print(palavra)

x = int(input("Digite um numero: "))
palavra = input('Digite uma palavra: ')

repetidor(x, palavra)
