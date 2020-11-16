"""

13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos.


"""


def main():

    prova1 = float(input('Digite a nota da primeira prova: '))
    prova2 = float(input('Digite a nota da segunda prova:'))
    prova3 = float(input('Digite a nota da terceira prova:'))

    media = (prova1 * 1 + prova2 * 1 + prova3 * 2) / (1+2)
    print(f'Resultado da média ponderada das notas informadas: {media}')


if __name__ == '__main__':
    main()
