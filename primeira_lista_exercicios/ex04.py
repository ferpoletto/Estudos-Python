#4 - Faça um programa que receba um valor que é o valor pago,
# um segundo valor que é o preço do produto e retorne o
# troco a ser dado.
#
# (modifique para receber um valor de desconto e
# subtraia do valor do produto)

class pagamento():

    def calcula_troco(self, valor_recebido, valor_produto):
        troco = valor_recebido - valor_produto
        if troco == 0:
            print('Não tem troco!')
        elif troco > 0:
            print(f'Devolver R${troco} de troco.')
        elif troco < 0 :
            print(f'Faltam R${troco*-1} para comprar o produto.')

valor_recebido = float(input("Digite o valor recebido: "))
valor_produto = float(input("Digite o valor do produto: "))

calculo = pagamento()
calculo.calcula_troco(valor_recebido, valor_produto)
