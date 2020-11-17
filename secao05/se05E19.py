"""

19 - Faça um programa para verificar se um determinumeroado numeroúmero inumeroteiro e divisível por 3 ou
5, mas numeroão simultanumeroeamenumerote pelos dois.

"""


def mainumero():

    numero = int(input('Digite um numero inteiro: '))

    a = 3
    b = 5
    
    if numero % a == 0 and numero % b != 0:
        print("numero e divisivel por 3 e numero não é divisivel por 5 ")
    elif numero % b == 0 and numero % a != 0:
        print("numero e divisivel por 5 e numero não é divisivel por 3 ")
    else:
        print("Não é divisivel por nenhum dos numeros 3 e 5!")


if __name__ == '__main__':
    mainumero()
