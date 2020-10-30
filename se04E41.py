"""

41- Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.

"""


def main():

    valor_hora = float(input('Digite o valor da hora de trabalho em reais R$: '))
    numero_horas_trabalhadas = int(input('Digite o numero de horas trabalhadas no mês: '))
    calc_horas = valor_hora * numero_horas_trabalhadas
    calc_horas_acrescimo = calc_horas * 0.10
    resultado = calc_horas + calc_horas_acrescimo

    print(f'Valor da hora de trabalho: {valor_hora}')
    print(f'Numero de horas trabalhadas: {numero_horas_trabalhadas}')
    print(f'Salario bruto: {calc_horas}')
    print(f' O Salário a ser pago com 10% de acrescimo: {resultado}')


if __name__ == '__main__':
    main()
