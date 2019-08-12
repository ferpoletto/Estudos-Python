palavras = ('FERNANDO', 'CARDERNO', 'ALFAFA')


for p in palavras:
    print(f'\nNa palavra {p} temos as vogais ', end='' )
    for letra in p:
        if letra.lower()in 'aeiou':
            print(letra, end=' ')
