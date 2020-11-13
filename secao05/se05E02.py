"""

2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.

"""
import math


def main():

    valor = int(input('Digite um valor: '))

    if valor > 0:
        print(f'Raiz quadradada do numero digitado:  {math.sqrt(valor)}')
    elif valor <= 0:
        print(f'Número é inválido!')


if __name__ == '__main__':
    main()
