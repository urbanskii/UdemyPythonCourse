"""

22- Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = 0.91*J, sendo J o comprimento em jardas e M o comprimento em metros.

"""


def main():

    valor_jardas = float(input('Digite o valor em jardas: '))
    valor_metros = valor_jardas*0.91
    print(f'Valor em jardas convertido para metros: {valor_metros}')


if __name__ == '__main__':
    main()
