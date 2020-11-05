"""

14 - Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G* π (Pi)/180, sendo G o Ângulo em graus
e R em radianos e π (Pi) = 3.14.

"""


def main():

    angulo = float(input('Digite um ângulo em graus: '))
    radiano = angulo * 3.14/180
    print(f'Resultado do ângulo em grausº convertido em radiano: {radiano}')


if __name__ == '__main__':
    main()
