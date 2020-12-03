"""

33 - Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de
acordo com a segunda tabela).

PREÇO ANTIGO	     PERCENTUAL DE AUMENTO
até R$ 50           	      5%
entre R$ 50 e R$ 100	      10%
acima de R$ 100	              15%

PREÇO NOVO	                     MENSAGEM
até R$ 80	                      Barato
entre R$ 80 e R$ 120 (inclusive)  Normal
entre R$ 120 e R$ 200 (inclusive) Caro
acima de R$ 200	                  Muito caro

"""


def main():

    try:
        preco = float(input('Informe o valor do produto R$: '))
        aumento = 0

        if int(preco) <= 50:
            aumento = preco * 0.05
            aumento = preco + aumento
        elif 50 < preco < 100:
            aumento = preco * 0.10
            aumento = preco + aumento
        elif preco > 100:
            aumento = preco * 0.15
            aumento = preco + aumento

        if aumento < 80:
            print(f'Barato {aumento}')
        elif 80 < aumento < 120:
            print(f'Normal {aumento}')
        elif 120 < aumento < 200:
            print(f'Caro {aumento}')
        elif aumento > 200:
            print(f'Muito Caro {aumento}')

    except ValueError as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    main()
