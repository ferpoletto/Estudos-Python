#32 - Lançar nota final para 3 alunos, deve ser possível adicionar, atualizar e deletar.
# Apresente o resultado somente a nota de cada aluno ao final das operações.

print('-='*20)
print(f'Lançamento de notas')
print('-='*20)

turma = list()
aluno = dict()

op = ''

def mostrar_turma():
    print('Essa turma é composta por: ')
    for i in range(len(turma)):
        print(f"{turma[i]['nome']}")

def atualizar_notas(find_nome):
    for e, i in enumerate(turma):
        if i['nome'] == find_nome:
            i['N1'] = float(input("Digite a N1: "))
            i['N2'] = float(input("Digite a N2: "))
            i['N3'] = float(input("Digite a N3: "))


def cadastrar_aluno():
    # Cria um dicionario com as informações do aluno
    aluno['nome'] = input("Digite o nome do aluno: ")

    aluno['N1'] = float(input("Digite a N1: "))
    aluno['N2'] = float(input("Digite a N2: "))
    aluno['N3'] = float(input("Digite a N3: "))

    # Coloca o aluno cadastrado dentro da lista Turma
    turma.append(aluno.copy())
    print('Aluno cadastrado com sucesso!')


def excluir_aluno(find_name):
    for e, i in enumerate(turma):
        if i['nome'] == find_name:
            turma.pop(e)


def verifica_media(find_nome):
    soma = 0
    for i in range(len(turma)):
        if turma[i]['nome'] == find_nome:
            soma = turma[i]['N1'] + turma[i]['N2'] + turma[i]['N3']
    print(f'A média do aluno é {(soma / 3):.2f}')


def mostrar_aluno(find_nome):
    for i in range(len(turma)):
        if turma[i]['nome'] == find_nome:
            print(f'Nome: {turma[i]["nome"]}\n'
                  f'N1: {turma[i]["N1"]}\n'
                  f'N2: {turma[i]["N2"]}\n'
                  f'N3: {turma[i]["N3"]}')

while True:
    op = int(input('\n'
                   '1 - Cadastrar um aluno\n'
                   '2 - Atualizar notas de um aluno\n'
                   '3 - Deletar um aluno\n'
                   '4 - Verificar média de um aluno\n'
                   '5 - Mostrar Turma\n'
                   '6 - Mostrar aluno\n'
                   '7 - SAIR\n'
                   'Digite a opção desejada: '))

    if op == 7:
        break

    elif op == 6:
        mostrar_turma()
        find_nome = input("Qual aluno deseja ver as notas? ")
        mostrar_aluno(find_nome)

    elif op == 5:
        mostrar_turma()

    elif op == 4:
        print('-=' * 20)
        print('Verificar média de um aluno')
        print('-=' * 20)
        mostrar_turma()
        find_nome = input("Qual aluno deseja verificar a média? ")
        verifica_media(find_nome)

    elif op == 3:
        print('-=' * 20)
        print('Deletar um aluno')
        print('-=' * 20)
        mostrar_turma()
        find_nome = input("Qual aluno deseja excluir da turma? ")
        excluir_aluno(find_nome)

    elif op == 2:
        print('-=' * 20)
        print('Atualizar notas de um aluno')
        print('-=' * 20)
        mostrar_turma()
        find_nome = input("Qual aluno deseja atualizar as notas? ")
        atualizar_notas(find_nome)

    else:
        print('-=' * 20)
        print('Cadastrar um aluno')
        print('-=' * 20)
        cadastrar_aluno()
        mostrar_turma()

