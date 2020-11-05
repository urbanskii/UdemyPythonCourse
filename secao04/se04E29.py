"""

29 - Leia quatro notas, calcule a média aritmética e imprima o resultado.


"""


def main():

    nota1 = float(input('Digite a primeira nota:  '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    media_notas = (nota1 + nota2 + nota3 + nota4)/4

    print(f'Resultado da média aritmética das notas informadas: {media_notas:.4}')


if __name__ == '__main__':
    main()
