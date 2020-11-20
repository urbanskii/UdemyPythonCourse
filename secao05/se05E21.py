"""

21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:

1. Soma de 2 números.
2. Diferença entre 2 números ( maior pelo menor).
3. Produto entre 2 números.
4. Divisão entre 2 números (o denominador não pode ser zero).
Opção:


"""


def main():

    while True:

        try:
            print('Escolha a opção:')
            print('1. Soma de 2 números.')
            print('2. Diferença entre 2 números ( maior pelo menor).')
            print('3. Produto entre 2 números.')
            print('4. Divisão entre 2 números (o denominador não pode ser zero).')
            print('5. Sair.')
            opcao = int(input('Opção: '))

            while True:
                if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
                    if opcao == 1:
                        try:
                            numero1 = int(input('Digite um numero: '))
                            numero2 = int(input('Digite outro numero: '))

                            if numero1 > 0 and numero2 > 0:
                                print(f'soma dos 2 valores: {numero1+numero2} \n')
                                break
                            else:
                                print('Valor incorreto!.\n')
                                break
                        except ValueError:
                            print('Valor incorreto!.\n')
                            break
                    elif opcao == 2:
                        try:
                            numero1 = int(input('Digite um numero: '))
                            numero2 = int(input('Digite outro numero: '))
                            if numero1 > numero2:
                                diferenca = numero1 - numero2
                                pass
                            else:
                                diferenca = numero2 - numero1
                                pass
                            print(f'A diferença entre os 2 valores: {diferenca} \n')
                            break
                        except ValueError:
                            print('Valor incorreto!.\n')
                            break
                    elif opcao == 3:
                        try:
                            numero1 = int(input('Digite um numero: '))
                            numero2 = int(input('Digite outro numero: '))

                            if numero1 > 0 and numero2 > 0:
                                print(f'Produto dos 2 valores: {numero1*numero2} \n')
                                break
                            else:
                                print('Valor incorreto!.\n')
                                break
                        except ValueError:
                            print('Valor incorreto!.\n')
                            break
                    elif opcao == 4:
                        try:
                            numero1 = int(input('Digite um numero: '))
                            numero2 = int(input('Digite outro numero: '))

                            if numero1 > 0 and numero2 > 0:
                                print(f'Divisão dos 2 valores: {numero1/numero2} \n')
                                break
                            else:
                                print('Valor incorreto!.\n')
                                break
                        except ValueError:
                            print('Valor incorreto!.\n')
                            break
                elif opcao == 5:
                    break
                else:
                    print('Opção invalida!.\n')
                    break
            if opcao == 5:
                break
        except ValueError:
            print('Opção invalida!.\n')


if __name__ == '__main__':
    main()
