"""

44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.

"""


def main():

    altura_degrau = float(input('Digite a altura do degrau: '))
    altura_desejada = float(input('Digite a altura desejada: '))
    degrau = 0
    quantidade_degrau = 0

    while altura_desejada != degrau:
        degrau = degrau + altura_degrau
        quantidade_degrau += 1

    print(f'Quantidade de degraus necessaria para altura desejada: {quantidade_degrau} ')


if __name__ == '__main__':
    main()
