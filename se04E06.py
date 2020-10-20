"""

6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
    A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
    e C a temperatura em Fahrenheit.

"""


def main():

    temperatura_celsius_input = float(input('Digite a temperatura em Celsius: '))
    temperatura_Fahrenheit = temperatura_celsius_input*(9.0/5.0)+32.0

    print(f'Temperatura Celsius convertida em Fahrenheit: {temperatura_Fahrenheit}')


if __name__ == '__main__':
    main()
