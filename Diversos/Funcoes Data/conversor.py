def converte_data_nascimento(data_nascimento):

    #Tupla que contem o nome dos meses por extenso. Tupla é um tipo de lista que tem como caracteristica princial ser imutável.
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro')

    # Utilizando o método SPLIT do Python, a string será dividida a cada '/', e adicionada nas variáveis respectivamente
    dia, mes, ano = data_nascimento.split('/')

    #Imprimir na tela a data formatada, buscando na Tupla meses o mes informado pelo usuario
    print(f'Você nasceu em {dia} de {meses[int(mes) - 1]} de {ano}')
