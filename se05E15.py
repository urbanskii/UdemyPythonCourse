"""

15 - Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/π (Pi), sendo G o Ângulo em graus
e R em radianos e π = 3.14

"""


def main():

    angulo_radiano = float(input('Digite o ângulo em Radiano: '))
    angulo_graus = angulo_radiano * 180/3.14

    print(f'Angulo em Radianos convertido em graus: {angulo_graus}')


if __name__ == '__main__':
    main()
