"""

29 - Faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a
pergunta: qual é a soma de a + b, onde a e b são os números aletatórios. Peça a
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.

"""
from random import randint
from random import randint


def main():
    x = 0
    try:
        while True:
            if x == 5:
                break
            n1 = randint(0, 100)
            n2 = randint(0, 100)
            print(f'Qual a soma dos numeros a seguir? {n1} + {n2} ')
            user = int(input('Digite a resposta: '))
            if user == n1 + n2:
                print(f'Sua resposta está correta: {user}! Resultado correto: {n1+n2}')
            else:
                print(f'Sua resposta está incorreta {user}! Resultado correto: {n1+n2}')
            x = x + 1
            print('-----------------------\n')

    except ValueError as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    main()

