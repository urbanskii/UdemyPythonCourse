"""

25- Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A formula
de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres.

"""


def main():

    valor_a_acres = float(input('Digite o valor da área em Acres: '))
    valor_m_quadrados = valor_a_acres * 4048.58
    print(f'Valor da área em acres convertido para metros quadrados m²: {valor_m_quadrados:.3f}')


if __name__ == '__main__':
    main()
