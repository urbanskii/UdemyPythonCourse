"""

25 - Calcule as raízes da equação de 2º grau.

Lembrando que:
\Large x=\frac{-b\pm\sqrt{\Delta}}{2a}

Onde
\Large;\Delta=B^2-4ac
E \Large;ax^2+bx+c=0 representa uma equação de 2ºgrau.
A variável tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não
é equação de segundo grau".

Se \Large;\Delta<0, não existe real, Imprima a mensagem Não existe raiz.

Se \Large;\Delta=0, existe uma raiz real, Imprima a raiz e a mensagem Raiz única.

Se \Large;\Delta\geq0, Imprima as duas raízes reais.

"""
import math


def main():

    try:
        a = float(input('Informe o valor de a: '))
        b = float(input('Informe o valor de b: '))
        c = float(input('Informe o valor de c: '))

        delta = (b**2 - 4*a*c)

        if delta < 0:
            print('Não existe raiz')
        elif delta == 0:
            print(f'Raiz unica {delta}')
        elif delta >= 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f'Raizes reais X1: {x1}')
            print(f'Raizes reais X2: {x2}')
    except ValueError as a:
        print(f'Erro: {a}')


if __name__ == '__main__':
    main()
