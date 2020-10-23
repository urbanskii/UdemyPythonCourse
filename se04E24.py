"""

24 - Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A fórmula
de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A a área em acres.

"""


def main():

    valor_m_quadrados = float(input('Digite o valor em metros quadrados m²: '))
    valor_acres = valor_m_quadrados * 0.000247
    print(f'Valor em metros convertido para jardas: {valor_acres}')


if __name__ == '__main__':
    main()
