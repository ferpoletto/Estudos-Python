#7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois,
# informe o menor número, o maior número, a soma dos números informados e a média aritmética
# números informados.

class operacoes():

    def calcula_media_aritmetica(self, lista):
        soma = operacoes()
        media = soma.calcula_soma(lista)/len(lista)
        return f'Média = {media}'

    def calcula_soma(self, lista):
        soma_dos_numeros = 0
        for numero in lista:
            soma_dos_numeros += numero
        return soma_dos_numeros

    def calcula_max_min(self, lista):
        maximo = max(lista)
        minimo = min(lista)
        retorno = [maximo, minimo]
        return f'Máximo = {retorno[0]} \nMínimo = {retorno[1]}'

lista = []
for i in range(10):
    lista.append(float(input(f'Digite o {i+1}o numero: ')))

minhaClasse = operacoes()

print(f'Soma = {minhaClasse.calcula_soma(lista)}')
print(minhaClasse.calcula_media_aritmetica(lista))
print(minhaClasse.calcula_max_min(lista))
