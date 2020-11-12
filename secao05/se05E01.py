"""
01 - Faça um programa que receba dois números e mostre qual deles é o maior.
"""


def main():

    valor1 = int(input("Digite o primeiro valor um numero inteiro: "))
    valor2 = int(input("Digite o segundo valor um numero inteiro: "))

    if valor1 > valor2:
        print(f'Valor 1 é maior {valor1}')
    elif valor2 > valor1:
        print(f'Valor 2 é maior {valor2}')
    elif valor1 == valor2:
        print(f'Os valores são iguais')


if __name__ == '__main__':
    main()
