"""

16 - Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.


"""


def main():

    dia = int(input('Informe um numero inteiro: '))

    if dia == 1:
        print(f'Mês do ano = Janeiro:  {dia}')
    elif dia == 2:
        print(f'Mês do ano = Fevereiro:  {dia}')
    elif dia == 3:
        print(f'Mês do ano = Março:  {dia}')
    elif dia == 4:
        print(f'Mês do ano = Abril:  {dia}')
    elif dia == 5:
        print(f'Mês do ano = Maio:  {dia}')
    elif dia == 6:
        print(f'Mês do ano = Junho:  {dia}')
    elif dia == 7:
        print(f'Mês do ano = Julho:  {dia}')
    elif dia == 8:
        print(f'Mês do ano = Agosto:  {dia}')
    elif dia == 9:
        print(f'Mês do ano = Setembro:  {dia}')
    elif dia == 10:
        print(f'Mês do ano = Outubro:  {dia}')
    elif dia == 11:
        print(f'Mês do ano = Novembro:  {dia}')
    elif dia == 12:
        print(f'Mês do ano = Dezembro:  {dia}')


if __name__ == '__main__':
    main()
