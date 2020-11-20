"""

20 - Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:

    - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.

    - Chama-se equilátero o triângulo que tem três lados iguais.

    - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.

    - Recebe o nome de escaleno o triângulo que tem os três lados diferentes,

"""


def main():

    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    c = int(input('Digite o terceiro valor: '))

    if a > 0 and b > 0 and c > 0:
        if a == b and a == c and b == c:
            print('Triângulo equilátero')
        elif a == b or a == c or b == c:
            print('Triangulo isósceles')
        elif a != b and a != c and b != c:
            print('Triângulo escaleno')
    else:
        print('Valor incorreto!.')


if __name__ == '__main__':
    main()
