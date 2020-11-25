"""

28 - Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

(a) Geométrica:	\Large;\sqrt[3]{x*y*z}
(b) Ponderada:	\Large;\frac{x+2*y+3*z}{6}
(c) Harmônica:	\Large;\frac{1}{\frac{1}{x}+\frac{1}{y}+\frac{1}{z}}
(d) Aritmética:	\Large;\frac{x+y+z}{3}

(a) Geometrica: ´√3 x ∗ y ∗ z
(b) Ponderada: x+2∗y+3∗z/6
(c) Harmonica: ˆ1/1/x + 1/y + 1/z
(d) Aritmetica: ´x+y+z/3

"""
import statistics


def main():

    try:
        while True:
            print('Escolha uma das médias abaixo pelo número: ')
            print('1 - Geométrica: ´√3 x ∗ y ∗ z')
            print('2 - Ponderada: x+2∗y+3∗z/6')
            print('3 - Harmônica: ˆ1/1/x + 1/y + 1/z')
            print('4 - Aritmética: ´x+y+z/3 ')
            print('5 - Sair')
            opcao = int(input('Opção: '))

            while True:
                if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
                    x = int(input('Informe o primeiro número inteiro positivo: '))
                    y = int(input('Informe o segundo número inteiro positivo: '))
                    z = int(input('Informe o terceiro número inteiro positivo: '))

                    if opcao == 1:
                        raiz = x*y*z
                        calc = raiz ** (1./3.)
                        print(f'Resultado: {calc:.3}')
                        break
                    elif opcao == 2:
                        calc = (x+(2*y)+(3*z))/6
                        print(f'Resultado: {calc:.3}')
                        break
                    elif opcao == 3:
                        calc = statistics.harmonic_mean([x, y, z])
                        print(f'Resultado: {calc:.3}')
                        break
                    elif opcao == 4:
                        calc = (x+y+z)/3
                        print(f'Resultado: {calc}')
                        print(f'Resultado1: {statistics.fmean([x, y, z])}')
                        break
                elif opcao == 5:
                    break
                else:
                    print('Opção incorreta!')
                    break
            if opcao == 5:
                break
    except ValueError as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    main()
