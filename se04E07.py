"""

7 - Leia um Temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius e F
a temperatura em Fahrenheit.

"""


def main():

    temperatura_fahrenheit_input = float(input('Digite a temperatura em Fahrenheit: '))
    temperatura_celsius_calc = 5.0*(temperatura_fahrenheit_input-32.0)/9.0

    print(f'Temperatura Fahrenheit convertido para Celsius: {temperatura_celsius_calc}')


if __name__ == '__main__':
    main()
