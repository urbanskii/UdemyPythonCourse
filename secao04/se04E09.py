"""

9 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.

"""


def main():
    temp_celsius = float(input('Digite a temperatura em Celsius: '))
    temp_kelvin = temp_celsius + 273.15

    print(f'A temperatura convertida em kelvin: {temp_kelvin}')


if __name__ == '__main__':
    main()
