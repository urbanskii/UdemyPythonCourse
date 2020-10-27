"""

27 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H
a área em hectares.

"""


def main():

    valor_a_hectares = float(input('Digite o valor de área em hectares: '))
    valor_a_metros = valor_a_hectares * 10000

    print(f'Valor de área em hectares convertido em metros quadrados m²: {valor_a_metros:.11}')


if __name__ == '__main__':
    main()
