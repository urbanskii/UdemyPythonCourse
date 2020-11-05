"""

45- Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCII para resolver o problema.


"""


def main():
    letra = input('Digite uma letra Maiúscula: ')
    letra_minuscula = chr(ord('a') + ord(letra) - ord('A'))
    print(f'Letra digitada minúscula: {letra_minuscula}')


if __name__ == '__main__':
    main()
