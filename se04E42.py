"""
42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base.
"""


def main():

    salario_base = float(input('Digite o sálario base: '))
    calc_gratificacao = salario_base * 0.05
    calc_gratificacao = salario_base - calc_gratificacao

    calc_imposto = salario_base * 0.07
    calc_imposto = salario_base - calc_imposto

    salario_base = salario_base - calc_imposto
    salario_base = salario_base + calc_gratificacao

    print(f'Salario liquido: {salario_base:.6}')
    print(f'Gratificação sobre o sálario 5%: {calc_gratificacao}')
    print(f'Desconto imposto 7%: {calc_imposto}')


if __name__ == '__main__':
    main()
