#1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não.
#   Receba os dados pela console e chame este método.

#   (modifique este exercício para receber 5 alunos, 3 notas para cada um e calcule a média mostrando se está aprovado ou não)

class validacao():

    def valida_idade_maior_18(self, idade):
        if idade >= 18:
            return("Maior de idade")
        else:
            return("Menor de idade")

    def executa(self):
        idade = validacao()
        print(idade.valida_idade_maior_18(int(input("Digite idade: "))))
