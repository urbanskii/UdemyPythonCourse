"""

34 - Leia o valor do raio de um círculo e calcule e imprima a área do circulo
correspondente. A área do círculo é π (Pi) * raio², considere π (pi) = 3.141592.


"""


def main():

    pi = 3.141592
    valor_raio = float(input('Digite o valor do raio de um circulo: '))
    area_circulo = pi*(valor_raio**2)

    print(f'Area do circulo correspondente: {area_circulo:.10}')


if __name__ == "__main__":
    main()
