"""

32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o
antecessor de seu dobro.

"""


def main():

    numero_inteiro = int(input('Informe um numero inteiro: '))
    triplo = numero_inteiro*3
    antecessor_dobro = (numero_inteiro*2)-1
    print(f'Resultado da soma entre o triplo do numero informado com o antecessor de seu dobro: {antecessor_dobro+triplo}')


if __name__ == '__main__':
    main()
