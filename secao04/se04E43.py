"""

43 - Escreva um programa de ajuda para vendedores. A partir de uma valor total lido, mostre:
o total a pagar com desconto de 10%;
o valor de cada parcela, no parcelamento de 3X sem juros;
a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

"""


def main():

    valor = float(input('Digite o valor: '))
    calc_desconto10 = valor * 0.10
    resultado1 = valor - calc_desconto10

    parcela_s_juros = resultado1/3

    calc_comissao1 = resultado1 * 0.05
    resul_comissao1 = resultado1 - calc_comissao1
    comissao1 = resultado1 - resul_comissao1

    calc_comissao2 = valor * 0.05
    resul_comissao2 = valor - calc_comissao2
    comissao2 = valor - resul_comissao2

    print(f'O valor com desconto de 10%: {resultado1}')
    print(f'Parcelado sem juros: {parcela_s_juros}')
    print(f'Comissão sobre o valor a vista: {comissao1}')
    print(f'Comissão sobre o valor parcelado: {comissao2}')


if __name__ == '__main__':
    main()
