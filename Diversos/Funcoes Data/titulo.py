#importanto o módulo datetime para usar a função date
from datetime import date


#Método que imprime na tela o cabecalho


def imprimirCabecalho():
    print(f'='*55)
    nome = 'Fernando Poletto'
    data_atual = date.today()
    data_formatada = data_atual.strftime('%d.%m.%Y')
    print(f'Teste prático referente a seleção de monitoria')
    print(f'Candidado a monitoria: {nome}')
    print(f'Data da execução do programa: {data_formatada}')
    print(f'=' * 55)
