"""

 8 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C=K-273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.

"""


def main():

    temp_kelvin = float(input('Digite a temperatura em Kelvin: '))
    temp_celsius = temp_kelvin-273.15

    print(f'Temperatura Kelvin convertida em Celsius: {temp_celsius}')


if __name__ == '__main__':
    main()
