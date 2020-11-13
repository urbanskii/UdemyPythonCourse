"""

07- Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem "Números iguais.".

"""


def main():

    valor1 = int(input('Digite um valor1: '))
    valor2 = int(input('Digite um valor2: '))

    if valor1 > valor2:
        print(f'Valor1 é maior do que valor2 : {valor1}')
    elif valor2 > valor1:
        print(f'Valor2 é maior do que valor1 :  {valor2}')
    elif valor2 == valor1:
        print(f'Os valores são iguais!')


if __name__ == '__main__':
    main()
