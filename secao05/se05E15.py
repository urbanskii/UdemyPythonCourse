"""

15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 7 imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.


"""


def main():

    dia = int(input('Informe um numero inteiro: '))

    if dia == 1:
        print(f'Dia da semana = Domingo:  {dia}')
    elif dia == 2:
        print(f'Dia da semana = Segunda-feira:  {dia}')
    elif dia == 3:
        print(f'Dia da semana = Terça-feira:  {dia}')
    elif dia == 4:
        print(f'Dia da semana = Quarta-feira:  {dia}')
    elif dia == 5:
        print(f'Dia da semana = Quinta-feira:  {dia}')
    elif dia == 6:
        print(f'Dia da semana = Sexta-feira:  {dia}')
    elif dia == 7:
        print(f'Dia da semana = Sábado:  {dia}')


if __name__ == '__main__':
    main()
