"""

20 - Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é: L = K/0.45 sendo K a massa em quilogramas e L a massa em libras.

"""


def main():

    valor_quilogramas = float(input('Digite o valor em quilogramas: '))
    valor_libras = valor_quilogramas/0.45
    print(f'Valor em quilogramas convertido para libras: {valor_libras}')


if __name__ == '__main__':
    main()
