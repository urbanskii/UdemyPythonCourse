"""

27 - Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:

Categoria	Idade
Infantil A	5 a 7
Infantil B	8 a 10
Juvenil A	11 a 13
Juvenil B	14 a 17
Sênior	maiores de 18 anos


"""


def main():

    idade = int(input('Informe a idade: '))

    if 5 <= idade <= 7:
        print(f'Infantil A:  {idade}')
    elif 8 <= idade <= 10:
        print(f'Infantil B: {idade}')
    elif 11 <= idade <= 13:
        print(f'Juvenil A: {idade}')
    elif 14 <= idade <= 17:
        print(f'Juvenil A: {idade}')
    elif idade >= 18:
        print(f'Sênior: {idade}')
    else:
        print('Idade incorreta!')


if __name__ == '__main__':
    main()
