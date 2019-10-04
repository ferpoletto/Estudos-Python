#10 - receba três notas de um aluno e informe se ele passou ou reprovou.

def verifica_aprovacao(n1, n2, n3):
    if ((n1 + n2 + n3) / 3) >= 7:
        print('Aprovado')
    else:
        print("Reprovado")


verifica_aprovacao(float(input("Digite a N1: ")),
                   float(input("Digite a N2: ")),
                   float(input("Digite a N3: ")))