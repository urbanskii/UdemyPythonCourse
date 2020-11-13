"""

09 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso
contrário imprima: Empréstimo concedido.

"""


def main():

    salario = float(input('Digite o salario: '))
    valor_prestacao = float(input('Valor da prestação: '))

    limite_salario = salario * 0.20

    if valor_prestacao < limite_salario:
        print(f'Emprestimo concedido!')
    else:
        print(f'Emprestimo ultrapassa 20% do salario!')


if __name__ == '__main__':
    main()
