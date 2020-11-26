"""

30 - Faça um programa que receba três números e mostre-os em ordem crescente.

"""


def main():

    n1 = int(input('Informe o primeiro Numero: '))
    n2 = int(input('Informe o segundo Numero: '))
    n3 = int(input('Informe o terceiro Numero: '))

    list_num = [n1, n2, n3]
    list_num.sort()
    print(f'Numeros em ordem crescente: {list_num}! os numeros informados {n1}, {n2}, {n3}')


if __name__ == '__main__':
    main()
