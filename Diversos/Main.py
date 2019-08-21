#função que converte a data de nascimento, que recebe uma variável como parametro
def converte_data_nascimento(data):

    #Tupla que contem o nome dos meses por extenso. Tupla é um tipo de lista que tem como caracteristica princial ser imutável.
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro')

    # Utilizando o método SPLIT do Python, a string será dividida a cada '/', e adicionada nas variáveis respectivamente
    dia, mes, ano = data_nascimento.split('/')

    #Imprimir na tela a data formatada, buscando na Tupla meses o mes informado pelo usuario
    print(f'Você nasceu em {dia} de {meses[int(mes) - 1]} de {ano}')


#Input da data do nascimento no formato string.
data_nascimento = str(input("\nDigite a data do seu nascimento [DD/MM/AAAA]: "))



#Chama a função que converte a data de nascimento e passa a variável data_nascimento como parametro.
converte_data_nascimento(data_nascimento)

print(f'\nFim da execução!')
