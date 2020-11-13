
"""

06 - Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.

"""


def main():

    valor1 = float(input('Digite um valor1: '))
    valor2 = float(input('Digite um valor2: '))

    if valor1 > valor2:
        print(f'Valor1 é maior do que valor2 e a diferença entre eles é :  {valor1 - valor2}')
    elif valor2 > valor1:
        print(f'Valor2 é maior do que valor1 e a diferença entre eles é :  {valor2 - valor1}')
    elif valor2 == valor1:
        print(f'Os valores são iguais!')


if __name__ == '__main__':
<<<<<<< main
    main()