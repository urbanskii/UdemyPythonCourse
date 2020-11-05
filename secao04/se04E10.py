"""

10- Leia uma velocidade em km/h (Quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em m/s.

"""

def main():

    velocidade_km_h = float(input('Digite a velocidade em Km/h: '))
    velocidade_metros_s = velocidade_km_h/3.6

    print(f'Velocidade em Km/h convertida em metros por m/s: {velocidade_metros_s}')


if __name__ == '__main__':
    main()
