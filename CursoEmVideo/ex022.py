nome = input('Digite seu nome: ')
print("Analisando seu nome...")
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
espaco = nome.find(' ')
print(f'Seu primeiro nome tem {espaco} letras')

separa = nome.split()
print(f'Seu nome do meio é {separa[1]}')



