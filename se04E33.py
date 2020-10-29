"""

33 - Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.

"""


def main():

    tamanho_lado_quadrado = int(input('Digite o tamanho do lado de um quadrao:'))
    area_quadrado = tamanho_lado_quadrado * tamanho_lado_quadrado

    print(f'Valor da area do quadrado: {area_quadrado}')


if __name__ == '__main__':
    main()
