palavra = input('Digite algo: ')

print(f'O tipo da variavel informada é: {type(palavra)}')
print(f'Só tem espaços? {palavra.isspace()}')
print(f'É um número? {palavra.isnumeric()}')
print(f'É alfabetico? {palavra.isalpha()}')
print(f'É alfabetico? {palavra.isalnum()}')
print(f'Está em maiuscula? {palavra.isupper()}')
print(f'Está em minúscula? {palavra.islower()}')
print(f'Está capitalizada? {palavra.istitle()}')
palavra.