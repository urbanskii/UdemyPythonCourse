"""

32 - Escrever um programa que leia o código do produto escolhido do cardápio de uma lan-
chonete e a quantidade. O Programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápio da lan-
chonete segue o padrão abaixo:

Especificação	Código	Preço
Cachorro Quente	100	    1.20
Bauru Simples	101	    1.30
Bauru com Ovo	102	    1.50
hamburguer	    103	    1.20
Cheeseburguer	104	    1.70
Suco	        105	    2.20
Refrigerante	106	    1.00


"""


def main():

    try:
        print('Especificação	    Código	Preço \n'
              'Cachorro Quente	    100	    1.20\n'
              'Bauru Simples	    101     1.30\n'
              'Bauru com Ovo	    102     1.50\n'
              'hamburguer          103     1.20\n'
              'Cheeseburguer	    104     1.70\n'
              'Suco                105     2.20\n'
              'Refrigerante	    106     1.00\n')
        codigo = float(input('Digite o código: '))
        quantidade = int(input('Digite a quantidade: '))

        if codigo == 100:
            print(f'Total: {quantidade*1.20}')
        elif codigo == 101:
            print(f'Total: {quantidade * 1.30}')
        elif codigo == 102:
            print(f'Total: {quantidade * 1.50}')
        elif codigo == 103:
            print(f'Total: {quantidade * 1.20}')
        elif codigo == 104:
            print(f'Total: {quantidade * 1.70}')
        elif codigo == 105:
            print(f'Total: {quantidade * 2.20}')
        elif codigo == 106:
            print(f'Total: {quantidade * 1.00}')
        else:
            print('Codigo inválido!')

    except ValueError as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    main()
