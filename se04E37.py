"""

37 -  Faça um programa que leia o valor de uma produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%.

"""


def main():

    valor_produto = float(input('Digite o valor do produto: '))
    valor_desconto = valor_produto*0.12
    print(f'Valor do Produto com desconto de 12%: {valor_produto-valor_desconto}')


if __name__ == '__main__':
    main()
