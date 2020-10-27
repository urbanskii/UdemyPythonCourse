"""

26 - Leia uma valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M*0.0001, sendo M a área em metros quadrados e H
a área em hectares.

"""


def main():

    valor_a_metros = float(input('Digite o valor de área em metros quadrados m²: '))
    valor_hectares = valor_a_metros * 0.0001

    print(f'Valor de área em metros quadrados m² convertido em hectares: {valor_hectares:.3}')


if __name__ == '__main__':
    main()
