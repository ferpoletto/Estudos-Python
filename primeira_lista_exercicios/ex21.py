# Crie uma classe chamada Ingresso que possui um valor em reais e um método
# imprimeValor().
# a. crie uma classe VIP, que herda Ingresso e possui um valor adicional. Crie um
# método que retorne o valor do ingresso VIP (com o adicional incluído).
# b. crie uma classe Normal, que herda Ingresso e possui um método que imprime:
# "Ingresso Normal".
# c. crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos
# para acessar e imprimir esta localização) e uma classe CamaroteSuperior, que é
# mais cara (possui valor adicional). Esta última possui um método para retornar o
# valor do ingresso. Ambas as classes herdam a classe VIPame o método  aumentaSalario de cada um.

#André Boa Sorte que fez

class Ingresso():
   def preco_ingresso(self):
        pass


class IngressoVip(Ingresso):
    def preco_ingresso(self):
        valor_ingresso = 200.00

        valor_temp=float(input("digite o valor adiciona do camarote vip com relação "
                               "ao ingresso normal {0:.2f} : ".format(valor_ingresso)))

        ingresso_vip = valor_temp + valor_ingresso

        print("o preço do ingresso VIP é {0:.2f}".format(ingresso_vip))

class IngressoNormal(Ingresso):
    def preco_ingresso(self):
        valor_ingresso = 200.00

        print("o preço do ingresso normal é de {0:.2f}".format(valor_ingresso))


class CamaroteInferior(Ingresso):
    def preco_ingresso(self):
        valor_ingresso = 200.00

        preco_temp=float(input('digite o preço adicional do camarote inferior com '
                               'relação ao preco normal de {0:.2f} : '.format(valor_ingresso)))

        local_cam_inf=input("digite o local onde se solcaliza o camarote inferior: ")

        cama_inf=preco_temp + valor_ingresso

        print("o preço do camarote inferior é de {0:.2f} e esta localizado: {1}"
              .format(cama_inf, local_cam_inf))

class CamaroteSuperior(Ingresso):
    def preco_ingresso(self):
        valor_ingresso = 200.00

        preco_temp = float(input('digite o preço adicional do camarote superior com'
                                  ' relação ao preco normal de {0:.2f} : '.format( valor_ingresso)))

        local_cam_sup = input("digite o local onde se solcaliza o camarote superior: ")

        cama_sup = preco_temp + valor_ingresso

        print("o preço do camarote superior é de {0:.2f} e esta localizado: {1}"
              .format(cama_sup, local_cam_sup))


while True:


    op = int(input("1- para o preço do ingreso normal\n"
                   "2- para o preço do ingreso VIP\n"
                   "3- para o preço do ingreso do camarote inferior\n"
                   "4- para o preço do ingreso do camarote superior\n"
                   "5- para sair\n"
                   "opção: "))

    if op == 1:
        normal = IngressoNormal()

        normal.preco_ingresso()

    elif op == 2:
        vip = IngressoVip()

        vip.preco_ingresso()

    elif op == 3:
        inferior = CamaroteInferior()

        inferior.preco_ingresso()

    elif op == 4:
        superior = CamaroteSuperior()

        superior.preco_ingresso()

    elif op == 5:
        break