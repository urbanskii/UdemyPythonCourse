"""

14- A nota final de uma estudante é calculada a partir de três notas atribuidas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliação Semestral 3; Exame Final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de
recuperação ( entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.


"""


def main():
    trabalho_laboratorio = float(input('Informe a nota do trabalho de laboratorio: '))
    avaliacao_semestral = float(input('Informe a nota da avaliação semestral: '))
    exame_final = float(input('Informe a nota do exame final: '))

    media_final = (trabalho_laboratorio*2 + avaliacao_semestral*3 + exame_final*5)/10

    if 0 <= media_final <= 2.9:
        print(f'Aluno reprovado! {media_final}')
    elif 3 <= media_final <= 4.9:
        print(f'Aluno em recuperação! {media_final}')
    elif 5 <= media_final <= 10:
        print(f'Aluno aprovado! {media_final}')
    else:
        print(f'Numero incorreto!')


if __name__ == '__main__':
    main()

