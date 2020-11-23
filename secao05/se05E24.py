"""


24 - Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
Faça um programa em que o usuário entre com o valor e o estado destino do produto
e o programa retorne o preço final do produto acrescido do imposto do estado em que ele
será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.


"""


def main():

    try:
        valor = float(input('Informe o valor do produto: '))
        estado = input('Informe o estado destino do produto: ')

        if estado == 'MG':
            valor_imposto = valor * 0.07
            valor = valor + valor_imposto
            print(f'Preço final do produto no envio para o Estado {estado}: {valor}')
        elif estado == 'SP':
            valor_imposto = valor * 0.12
            valor = valor + valor_imposto
            print(f'Preço final do produto no envio para o Estado {estado}: {valor}')
        elif estado == 'RJ':
            valor_imposto = valor * 0.15
            valor = valor + valor_imposto
            print(f'Preço final do produto no envio para o Estado {estado}: {valor}')
        elif estado == 'MS':
            valor_imposto = valor * 0.8
            valor = valor + valor_imposto
            print(f'Preço final do produto no envio para o Estado {estado}: {valor}')
        else:
            print('Valor incorreto!')
    except ValueError:
        print('Valor incorreto!')


if __name__ == '__main__':
    main()
