"""

17 - Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

\Large x=\frac{(basemaior+basemenor)*altura}{2}

Lembre-se a base maior e a base menor devem ser números maiores que zero.


"""


def main():

    basemaior = float(input('Informe a base maior: '))
    basemenor = float(input('Informe a base menor: '))
    altura = float(input('Informe a altura: '))

    if basemaior and basemenor > 0:
        area_trapezio = (basemaior+basemenor) * altura / 2
        print(f'Área do trapézio: {area_trapezio}')
    else:
        print(f'Valores invalidos!')


if __name__ == '__main__':
    main()
