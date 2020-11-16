"""

11 - Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor
8 (2 + 5 +1). Se o número lido não for maior do que zero, o programa terminará com a
mensagem "Número inválido".

"""


def main():

    numero = input('Digite um numero inteiro: ')

    if int(numero) > 0:
        primeiro_algarismo = int(numero[0])
        segundo_algarismo = int(numero[1])
        terceiro_algarismo = int(numero[2])
        inteiros_lista = [primeiro_algarismo, segundo_algarismo, terceiro_algarismo]

        print(f'A soma dos algarismos do numero digitado é: {sum(inteiros_lista)}')

    else:
        print('Número inválido.')


if __name__ == '__main__':
    main()
