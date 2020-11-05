"""

52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcio-
nalmente ao valor que cada um deu para a realização da aposta. Faça um programa que leia
quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do
prêmio com base no valor investido.


"""


def main():

    valor_investido1 = float(input('Digite o valor investido1: '))
    valor_investido2 = float(input('Digite o valor investido2: '))
    valor_investido3 = float(input('Digite o valor investido3: '))
    premio = float(input('Digite o valor do premio: '))

    valor_investido_total = valor_investido1 + valor_investido2 + valor_investido3
    valor_recebido1 = premio * valor_investido1 / valor_investido_total
    valor_recebido2 = premio * valor_investido2 / valor_investido_total
    valor_recebido3 = premio * valor_investido3 / valor_investido_total

    print(f'Valor investido: {valor_investido1:.4}' + f' Valor recebido: {valor_recebido1:.6}')
    print(f'Valor investido: {valor_investido2:.4}' + f' Valor recebido: {valor_recebido2:.6}')
    print(f'Valor investido: {valor_investido3:.4}' + f' Valor recebido: {valor_recebido3:.6}')


if __name__ == '__main__':
    main()
