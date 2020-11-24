"""

26 - Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em KM/l e escreva uma mensagem de acordo com
a tabela abaixo:

CONSUMO	(Km/l)	MENSAGEM
menor que	8	Venda o carro!
entre	8 e 14	Econômico!
maior que	12	Super Econômico!

"""


def main():

    try:
        km = float(input('Informe a distância em KM: '))
        quantidade_litros = float(input('Informe a quantidade de litros de gasolina consumidos: '))

        consumo = km / quantidade_litros

        if consumo < 8:
            print(f'venda o carro! {consumo:.3}')
        elif 8 < consumo < 14:
            print(f'Econômico! {consumo:.3}')
        elif consumo > 12:
            print(f'Super Econômico! {consumo:.3}')
        else:
            print('Erro')
    except ValueError as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    main()
