"""
39- A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
O primeiro ganhador receberá 46%;
O segundo receberá 32%;
O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.

"""


def main():

    valor = 780000.00
    valor1 = valor
    primeiro_ganhador = valor * 0.46
    resul_primeiro_ganhador = valor - primeiro_ganhador
    
    valor = valor - resul_primeiro_ganhador
    segundo_ganhador  = valor * 0.32
    resul_segundo_ganhador = valor - segundo_ganhador
    
    valor = valor - resul_segundo_ganhador
    resul_terceiro_ganhador = valor  
    print(f'Valor do prêmio: {valor1}')
    print(f'Resultado do primeiro ganhador 46% do prêmio: {resul_primeiro_ganhador}')
    print(f'Resultado do segundo ganhador 32% do premio: {resul_segundo_ganhador}')
    print(f'Resultado do terceiro ganhador 22% do prêmio : {resul_terceiro_ganhador}')
      

if __name__ == '__main__':
    main()

