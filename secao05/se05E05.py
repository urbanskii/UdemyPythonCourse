"""

5 - Faça um programa que receba um número inteiro e verifique se este número é par ou
ímpar.

"""


def main():
    valor = int(input('Digite um numero inteiro: '))

    if (valor % 2) == 0:
        print("Par")
    else:
        print("Ímpar")


if __name__ == '__Main__':
    main()
