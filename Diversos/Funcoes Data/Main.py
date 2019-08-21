from titulo import imprimirCabecalho
from conversor import converte_data_nascimento

#Entrada da data de nascimento pelo console. Está sendo validado o formato do input com a estrutura while True para que seja solicitado a entrada até que esteja no formato correto
while True:
    try:
        data_nascimento = str(input("\nDigite a data do seu nascimento [DD/MM/AAAA]: ")).strip()
        dia, mes, ano = data_nascimento.split('/')
        if (0 < int(dia) <= 31 and 0 < int(mes) <= 12 and 0 < len(ano) == 4 and data_nascimento[2] == data_nascimento[5] == '/'):
            break
    except:
        print('Você digitou a data incorretamente. Tente novamente')

#Chama a função que imprime o cabecalho
imprimirCabecalho()

#Chama a função que converte a data de nascimento e passa a variável data_nascimento como parametro para a conversão.
converte_data_nascimento(data_nascimento)

print(f'\nFim da execução!')
