"""

50 - Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual.

"""


def main():

    idade = int(input('Digite a idade: '))
    ano_atual = int(input('Digite o ano atual: '))
    print(f'Ano de nascimento: {ano_atual-idade}')


if __name__ == '__main__':
    main()
