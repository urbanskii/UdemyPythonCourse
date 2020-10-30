"""

38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%.

"""


def main():


    fun_salario = float(input('Digite o salario: ' ))
    aumento = fun_salario*0.25
    novo_salario = aumento+fun_salario
    print(f'Resultado do salario com aumento de 25%: {novo_salario:.6}')
    

if __name__ == '__main__':
    main()

