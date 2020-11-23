"""

23 - Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo:
1988, 1992, 1996


"""


def main():

    ano = int(input('informe o ano no formato aaaa: '))

    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        print(f'É um ano bissexto {ano}')
    else:
        print('Não é bissexto!')


if __name__ == '__main__':
    main()
