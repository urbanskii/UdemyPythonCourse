"""

17 - Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.

"""


def main():

    comrimento_centimetros = float(input('Digite o comprimento em centímetros: '))
    comprimento_polegadas = comrimento_centimetros/2.54

    print(f'Comprimento em centímetros convertido em polegadas: {comprimento_polegadas}')


if __name__ == '__main__':
    main()
