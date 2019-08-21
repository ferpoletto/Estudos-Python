from datetime import date


def imprimirCabecalho():
    print(f'='*40)
    nome = 'Fernando Poletto'
    data_atual = date.today()
    data_formatada = data_atual.strftime('%d.%m.%Y')
    print(f'Candidado a monitoria: {nome}')
    print(f'Data da execução do programa: {data_formatada}')
    print(f'=' * 40)




