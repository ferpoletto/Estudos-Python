#31 - Crie um dict com 5 nomes e profissões e remova o ultimo elemento

pessoas = {}
aux = {}

for i in range(3):
    aux.clear()
    aux = {input('Digite o nome: '): input("Digite profissao: ")}
    pessoas.update(aux.copy())

print(f"Primeiro dicionário: {pessoas}")

pessoas.popitem()

print(f"Dicionário após exclusão: {pessoas}")

