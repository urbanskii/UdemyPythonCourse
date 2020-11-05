"""

53 - Faça um Programa para ler as dimensões de um terreno (comprimento c e largura L),
bem como o preço do metro de tela p, Imprima o custo para cercar este mesmo terreno
com tela.

"""


def main():

    comprimento = float(input('Digite o comprimento do terreno: '))
    largura = float(input('Digite a largura do terreno: '))
    preco_tela = float(input('Digite o preco da tela: '))

    custo = comprimento * largura * preco_tela
    print(f'O custo para cercar o terreno: {custo}')


if __name__ == '__main__':
    main()
