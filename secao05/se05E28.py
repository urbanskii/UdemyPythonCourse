"""

28 - Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

(a) Geométrica:	\Large;\sqrt[3]{x*y*2}
(b) Ponderada:	\Large;\frac{x+2*y+3*z}{6}
(c) Harmônica:	\Large;\frac{1}{\frac{1}{x}+\frac{1}{y}+\frac{1}{z}}
(d) Aritmética:	\Large;\frac{x+y+z}{3}

"""


def main():

    try:
        while True:
            numero1 = int(input('Informe o primeiro número inteiro positivo: '))
            numero2 = int(input('Informe o segundo número inteiro positivo: '))
            numero3 = int(input('Informe o terceiro número inteiro positivo: '))


    except ValueError as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    main()
