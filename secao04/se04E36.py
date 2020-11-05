"""

36- Leia a altura e o raio de uma cilindro circular e imprima o volume do cilindro.
O volume de uma cilindro circular é calculado por meio da seguinte fórmula:
    V = π(pi) * raio² * altura, onde π(pi) = 3.141592.

"""

def main():

    pi = 3.141592
    print('Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.')
    altura = float(input('Informe a altura: '))
    raio = float (input('Informe o raio: '))
    raio = raio**2
    volume_cilindro = pi * (raio * altura)
     
    print(f'Volume do cilindro: {volume_cilindro}')


if __name__ == '__main__':
    main()

