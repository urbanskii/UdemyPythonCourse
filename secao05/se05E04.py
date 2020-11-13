"""

04 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
* O número digitado ao quadrado
* A raiz quadrada do número digitado

"""
import math


def main():

    valor = float(input('Digite um valor: '))

    if valor > 0:
        print(f'Numero digitado ao quadrado:  {valor**2}')
        print(f'Raiz quadrada do numero digitado:  {math.sqrt(valor)}')
    elif valor <= 0:
        print(f'Número invalido!: {valor}')


if __name__ == '__main__':
    main()
