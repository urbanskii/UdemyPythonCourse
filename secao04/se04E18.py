"""

18- Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos.

"""


def main():

    volume_m_cubicos = float(input('Digite o valor em metros cúbicos m³: '))
    volume_litros = 1000 * volume_m_cubicos
    print(f'O valor de metros cubicos convertido em Litros: {volume_litros}')


if __name__ == '__main__':
    main()
