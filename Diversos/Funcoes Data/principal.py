from titulo import imprimirCabecalho
from conversor import converte_data_nascimento


#Estrutura de repetição de loop infinito. Sairá do loop comente quando chegar no Break
while True:
    #Validação que verificará se a data está no formato correto [DD/MM/AAAA]
    try:
        # Entrada da data de nascimento pelo console.
        data_nascimento = str(input("\nDigite a data do seu nascimento [DD/MM/AAAA]: ")).strip()
        dia, mes, ano = data_nascimento.split('/')

        #Condição que verifica se o dia digitado é menor que 31 e maior de 0, se o mes é maior que 0 e menor de 12 e se o ano tem 4 digitos
        if (len(data_nascimento) == 10 and 0 < int(dia) <= 31 and 0 < int(mes) <= 12 and 0 < len(ano) == 4 and data_nascimento[2] == data_nascimento[5] == '/'):
            break
        else:
            print('Você digitou a data no incorretamente. Tente novamente')
    except:
        print('Você digitou a data incorretamente. Tente novamente')

#Chama a função que imprime o cabecalho
imprimirCabecalho()

#Chama a função que converte a data de nascimento e passa a variável data_nascimento como parametro para a conversão.
converte_data_nascimento(data_nascimento)

print(f'\nFim da execução!')
