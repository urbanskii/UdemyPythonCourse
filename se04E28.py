"""

28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos
três valores lidos.

"""


def main():

    valor1 = int(input('Digite o primeiro valor, um numero inteiro: '))
    valor2 = int(input('Digite o segundo valor, um numero inteiro: '))
    valor3 = int(input('Digite o terceiro valor, um numero inteiro: '))

    soma_quadrados_valores = (valor1**2) + (valor2**2) + (valor3**2)

    print(f'Resultado da soma dos quadrados dos numeros informados: {soma_quadrados_valores}')


if __name__ == '__main__':
    main()
