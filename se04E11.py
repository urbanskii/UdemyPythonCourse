"""

11 - Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é K = M*3.6, sendo K a velocidade
em km/h e M em m/s.

"""


def main():

    velocidade_metros_s = float(input('Digite a velocidade em m/s: '))
    velocidade_km_s = velocidade_metros_s*3.6

    print(f'A velocidade convertida em Km/h: {velocidade_km_s}')


if __name__ == '__main__':
    main()
