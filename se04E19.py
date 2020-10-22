"""

19 - Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A
fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos.

"""


def main():

    volume_litros = float(input('Digite um valor de volume em litros: '))
    volume_m_cubicos = volume_litros/1000
    print(f'O valor de volume em litros convertido para metros cubicos M³: {volume_m_cubicos}')


if __name__ == '__main__':
    main()
