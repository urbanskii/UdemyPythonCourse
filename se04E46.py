"""

46 - Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido, Exemplo:
Númerolido = 123
NúmeroGerado = 321.

"""


def main():

    numero = input('Digite o numero de 3 digitos: ')
    print(f'Númerolido: {numero}')
    print(f'Número Gerado: {numero[::-1]}')


if __name__ == '__main__':
    main()
