"""

18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações ma-
temáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu pro-
grama então pede dois valores numéricos e realiza a operação, mostrando o resultado e
saindo.

"""


def main():

    while True:
        print('Escolha uma das opções abaixo:')
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')
        escolha = int(input('Digite uma opção: '))

        while True:
            if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4 or escolha == 5:
                if escolha != 5:
                    valor1 = int(input('Digite um valor numérico: '))
                    valor2 = int(input('Digite outro valor numérico: '))
                    if escolha == 1:
                        print(f'Resultado da Adição: {valor1 + valor2}\n')
                        break
                    elif escolha == 2:
                        print(f'Resultado da Subtração: {valor1 - valor2}\n')
                        break
                    elif escolha == 3:
                        print(f'Resultado da Multiplicação: {valor1 * valor2}\n')
                        break
                    elif escolha == 4:
                        print(f'Resultado da Divisão: {valor1 / valor2}\n')
                        break
                else:
                    break
            elif escolha == 5:
                break
            else:
                print('Opção invalida! \n')
                break
        if escolha == 5:
            break


if __name__ == '__main__':
    main()
