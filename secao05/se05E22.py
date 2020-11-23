"""

22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são

    - Ter pelo menos 65 anos,

    - Ou ter trabalhado pelo menos 30 anos,

    - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

"""


def main():

    idade = int(input('Informe a idade: '))
    tempo_servico = int(input('Tempo de serviço: '))

    try:
        if idade > 65 or tempo_servico > 30:
            print(f'Aposentadoria liberada! {idade}{tempo_servico}')
        elif idade >= 60 and tempo_servico >= 25:
            print('Aposentadoria liberada!')
        else:
            print('Aposentadoria negada!')
    except ValueError:
        print('Valor incorreto!')


if __name__ == '__main__':
    main()
