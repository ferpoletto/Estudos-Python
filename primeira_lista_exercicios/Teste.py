turma = [{'nome': 'Fer', 'N1': 10, 'N2': 5, 'N3': 5}, {'nome': 'A', 'N1': 10, 'N2': 5, 'N3': 5}]

print(turma)

for i in range(len(turma)):
    for k in i.values():
        if k == 'Fer':
            print('achei')


print(turma)