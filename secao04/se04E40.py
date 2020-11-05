"""

40-Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.

"""


def main():

    valor_dia = 30.00
    dias_trabalhados = int(input('Informe os dias trabalhados: '))
    salario_bruto = valor_dia * dias_trabalhados

    calc = salario_bruto * 0.08
    salario_liquido = salario_bruto - calc

    print(f' Dias trabalhados: {dias_trabalhados}')
    print(f' Salario bruto: {salario_bruto:.5}')
    print(f' Salario liquido: {salario_liquido:.5}')


if __name__ == '__main__':
    main()
