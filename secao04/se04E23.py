"""

23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula
de conversão é: J = M/0.91 sendo J o comprimento em jardas e M o comprimento em metros.

"""


def main():

    valor_metros = float(input('Digite o valor em metros: '))
    valor_jardas = valor_metros/0.91
    print(f'Valor em metros convertido para jardas: {valor_jardas}')


if __name__ == '__main__':
    main()
