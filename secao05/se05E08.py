"""

8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um
valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido. este fato deve ser
informadao ao usuário e o programa termina.

"""


def main():

    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    if 0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
        print(f'A média das notas digitadas :  {(nota1 + nota2)/2}')
    else:
        print(f'Nota com valor incorreto!')


if __name__ == '__main__':
    main()
