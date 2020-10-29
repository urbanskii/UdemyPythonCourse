"""

35- Seja a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = √(a^2+b^2 ). Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.


"""
from math import sqrt


def main():

    print('Seja a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: √(a^2+b^2 )')
    a = int(input('Informe o valor do cateto a: '))
    b = int(input('informe o valor do cateto b: '))
    calculo_hipotenusa = (a**2)+(b**2)

    print(f'Resultado do calculo: {sqrt(calculo_hipotenusa)}')


if __name__ == '__main__':
    main()
