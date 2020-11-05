"""

49 - Faça um programa para que leia o horário (hora, minuto e segundo) de Inicio e a duração,
em segundos, de uma experiência biológica. O Programa deve resultar como o novo horário
(hora, minuto e segundo) do termino da mesma.

"""


def main():

    hora = input('Digite a hora: ')
    minuto = input('Digite o minuto: ')
    segundo = input('Digite os segundos: ')
    inicio = hora + ':' + minuto + ':' + segundo

    segundos = int(input('Digite os segundos: '))

    dias = segundos // 86400
    segundos_rest = segundos % 86400
    horas = segundos_rest // 3600
    segundos_rest = segundos_rest % 3600
    minutos = segundos_rest // 60
    segundos_rest = segundos_rest % 60

    ht = horas + int(hora)
    mt = minutos + int(minuto)
    st = segundos_rest + int(segundo)
    if st >= 60:
        mt = mt + 1
        st = st - 60
    if mt >=60:
        ht = ht + 1
        mt = mt - 60

    h_final = str(ht) + ':' + str(mt) + ':' + str(st)
    print(f'Horario de inicio: {inicio}')
    print(f'Fim da experiência: {h_final}')


if __name__ == '__main__':
    main()
