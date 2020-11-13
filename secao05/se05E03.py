"""

03 - Leia um numero real. Se o número positivo imprima a raiz quadrada. Do contrário,
imprima o numero ao quadrado.

"""
import math


def main():

    valor = float(input('Digite um valor: '))

    if valor > 0:
        print(f'Raiz quadradada do numero digitado:  {math.sqrt(valor)}')
    elif valor <= 0:
        print(f'Número ao quadrado: {valor**2}')


if __name__ == '__main__':
    main()

