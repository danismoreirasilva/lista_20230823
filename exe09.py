
while True:

    while True:
        paisA = int(input('Digite a população do país A: '))
        if paisA <= 0:
            print(f'Erro: O tamanho da população de A deve ser > do que zero!')
        else:
            break

    while True:
        taxaA = float(input('Digite a taxa de crescimento do país A: '))
        if 1 <= taxaA <= 100:
            break
        else:
            print(f'Erro: A taxa deve ser informada com valor entre 1 e 100%!')

    while True:
        paisB = int(input('Digite a população do país B: '))
        if paisB > paisA:
            break
        else:
            print(f'Erro: O tamanho da população de B deve ser > do que o pais A!')

    while True:
        taxaB = float(input('Digite a taxa de crescimento do país B: '))
        if 1 <= taxaB <= 100:
            break
        else:
            print(f'Erro: A taxa deve ser informada com valor entre 1 e 100%!')

    anos = 0
    while paisA < paisB:
        paisA *= 1 + (taxaA / 100)
        paisB *= 1 + (taxaB / 100)
        anos += 1

    print(f'Serão necessários {anos} anos para o país A ultrapassar ou igualar a população do país B.')

    while True:
        repetir = str(input('Deseja repetir a operação: S ou N: ')).lower()
        if repetir != 's' and repetir != 'n':
            print(f'Erro: Digite apenas S ou N!')
        else:
            break
    if repetir == 'n':
        print(f'Você saiu do programa!')
        break