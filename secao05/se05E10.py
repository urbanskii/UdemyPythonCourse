"""

10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
* Homens: (72.7 * h) - 58
* Mulheres: (62,1 * h) - 44,7

"""


def main():

    altura = float(input('Digite a altura: '))
    sexo = input('Digite o sexo: ')

    if sexo[:1].lower() == 'm':
        print(f'Peso ideal: {(72.7*altura) - 58:.4}')
    elif sexo[:1].lower() == 'f':
        print(f'Peso ideal: {(62.1 * altura) - 44.7:.4}')
    else:
        print(f'Informe corretamente!')


if __name__ == '__main__':
    main()
