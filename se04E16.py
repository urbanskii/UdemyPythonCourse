"""

16- Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
a Fórmula de conversão é: C = P * 2,54 sendo C o comprimento em centimetros e P o
comprimento em polegadas.

"""


def main():

    comprimento_polegadas = float(input('Informe o comprimento em polegadas: '))
    comprimento_centimetros = comprimento_polegadas * 2.54

    print(f'Comprimento em Polegadas convertido em centimetros: {comprimento_centimetros}')


if __name__ == '__main__':
    main()
