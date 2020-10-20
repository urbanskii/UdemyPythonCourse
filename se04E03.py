"""

3- Peça ao usuário para digitar trẽs valores inteiros e imprima a soma deles.

"""


def main():

    primeiro_valor = int(input("Digite o primeiro numero inteiro: "))
    segundo_valor = int(input("Digite o segundo valor inteiro: "))
    tercerio_valor = int(input("Digite o terceiro valor: "))
    valores = primeiro_valor, segundo_valor, tercerio_valor

    print(f'Resultado da soma dos valores: {primeiro_valor + segundo_valor + tercerio_valor}')


if __name__ == '__main__':
    main()
