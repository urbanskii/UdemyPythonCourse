"""

21 -Leia uma valor de massa em libras e apresente-o em quilogramas. A fórmula
de conversão é: K = L*0.45, sendo K a massa em quilogramas e L a massa em libras.

"""


def main():
    valor_libras = float(input('Digite o valor em libras: '))
    valor_quilogramas = valor_libras*0.45
    print(f'Valor em libras convertido para quilogramas: {valor_quilogramas}')


if __name__ == '__main__':
    main()
