"""

31 - Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostre qual a classificação dessa pessoa.

Altura	                           Peso
                 Até 60	  Entre 60 e 90 (Inclusive)	  Acima de 90
Menor que 1,20     A	            D	                   G
De 1,20 a 1,70	   B	            E	                   H
Maior que 1,70	   C	            F                      I


"""


def main():

    while True:
        try:
            altura = float(input('Digite a altura: '))
            peso = float(input('Digite o peso: '))

            if altura < 1.20:
                if peso <= 60:
                    print(f'Classificação A')
                elif 60 <= peso <= 90:
                    print(f'Classificação D')
                elif peso > 90:
                    print(f'Classificação G')
            elif 1.20 < altura < 1.70:
                if peso <= 60:
                    print(f'Classificação B')
                elif 60 <= peso <= 90:
                    print(f'Classificação E')
                elif peso > 90:
                    print(f'Classificação H')
            elif altura >= 1.70:
                if peso <= 60:
                    print(f'Classificação C')
                elif 60 <= peso <= 90:
                    print(f'Classificação F')
                elif peso > 90:
                    print(f'Classificação I')

        except ValueError as e:
            print(f'Erro: {e}')
            break


if __name__ == '__main__':
    main()
