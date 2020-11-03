"""

47 - Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

"""


def main():
    numero_inteiro = input('Digite um número inteiro de 4 dígitos (de 1000 a 9999): ')
    for p in numero_inteiro:
        print(f'Numero: {p}')


if __name__ == '__main__':
    main()
