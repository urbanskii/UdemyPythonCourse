"""

30 - Leia um valor em real e a cotação do dolar. Em seguida, imprima o valor correspondente
em dólares.

"""


def main():

    valor_real = float(input('Informe o valor em R$ Real: '))
    cotacao_dolar = float(input('Informe a cotação do dolar: '))

    print(f'Resultado da conversão de R$ Reais em US$ Dolares: {valor_real/cotacao_dolar:.5} ')


if __name__ == '__main__':
    main()
