"""

51 - Escreva um progama que leia as coordenadas xe y de pontos no R² e calcule sua distância
da origem (0, 0).

"""
import math


def main():

    x = float(input('Digite a coordenada X: '))
    y = float(input('Digite a coordenada Y: '))

    r = math.sqrt(math.pow(x,2) + math.pow(y,2))
    print(f'A distância é : {r}')


if __name__ == '__main__':
    main()
