alunos = {'Nome': input("Digite o nome do aluno: "),
          'Media': float(input('Digite a média do aluno: ')),
          'Situacao': ''}
'''
alunos = dict()
alunos['Nome'] = str(input("Digite o nome: "))
alunos['Media'] = float(input("Digite a media: '))


'''

if alunos['Media'] >= 7:
    alunos['Situacao'] = 'Aprovado'
elif alunos['Media'] < 7  and alunos['Media'] >= 5:
    alunos['Situacao'] = 'Recuperação'
else:
    alunos['Situacao'] = 'Reprovado'

print(f'O aluno {alunos["Nome"]} tem a média {alunos["Media"]} e por isso está {alunos["Situacao"]}')
print('-='*30)
for k, v in alunos.items():
    print(f'{k} = {v}')