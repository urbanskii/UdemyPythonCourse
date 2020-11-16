"""

12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número
inválido". Se o número for positivo, calcular o logaritmo deste numero.


"""
import math


def main():

    numero = int(input('Digite um numero inteiro: '))

    if numero > 0:
        print(f'A soma dos algarismos do numero digitado é: {math.log(numero, 10)}')
    else:
        print('Número inválido.')


if __name__ == '__main__':
    main()
