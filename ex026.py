frase = str(input("Digite uma frase: ")).strip()

print(f'A letra A aparece {frase.lower().count("a")} vezes na frase.\n'
      f'A primeira letra A apareceu na posição {frase.lower().find("a")}\n'
      f'A última letra A apareceu na posição {frase.lower().rfind("a")}\n')